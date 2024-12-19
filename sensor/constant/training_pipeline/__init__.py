import os

TRAGET_COLUMN="class"
PIPLELINE_NAME="sensor"
ARTIFAT_DIR="artifact"
FILE_NAME="senosr.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

PREPROCESSING_OBJECT_FILE_NAME="precprocessing.pkl"
MODEL_FILE_NAME="model.pkl"
SCHEMA_FILE_PATH=os.path.join("config","schema.yaml")
SCHEMA_DROP_COLS="drop_columns"

DATA_INGESTION_COLLECTION_NAME:str="aps"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2

