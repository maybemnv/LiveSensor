from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from starlette.responses import RedirectResponse, Response
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.ml.model.estimator import ModelResolver, TargetValueMapping
from sensor.utils.main_utils import load_object, read_yaml_file
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from sensor.constant.application import APP_HOST, APP_PORT
from sensor.logger import logging
from fastapi.middleware.cors import CORSMiddleware
import os
import pandas as pd
from io import StringIO

# Set environment variables
env_file_path = os.path.join(os.getcwd(), "env.yaml")

def set_env_variable(env_file_path):
    if os.getenv('MONGO_DB_URL', None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL'] = env_config['MONGO_DB_URL']

# Initialize FastAPI
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route that redirects to docs
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# Train route (asynchronous task for training)
@app.get("/train")
async def train_route(background_tasks: BackgroundTasks):
    try:
        train_pipeline = TrainPipeline()

        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")

        # Run training in the background
        background_tasks.add_task(run_training_pipeline)
        return Response("Training started in the background.")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

def run_training_pipeline():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        logging.exception(f"Error during training: {e}")

# Predict route (handles CSV upload for prediction)
@app.post("/predict")
async def predict_route(file: UploadFile = File(...)):
    try:
        # Read CSV file
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        # Load the best model
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")

        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)

        # Predict
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(), inplace=True)

        # Return prediction result as CSV
        result_csv = df.to_csv(index=False)
        return Response(content=result_csv, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=predictions.csv"})

    except Exception as e:
        return Response(f"Error Occurred: {e}")

# Main function to run the app (for local execution)
def main():
    try:
        set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        logging.exception(f"Error occurred: {e}")

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)

