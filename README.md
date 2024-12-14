APS Sensor Detection: Predictive Maintenance Model
Problem Statement
The Air Pressure System (APS) in heavy-duty vehicles is essential for crucial functions like braking and gear shifts. Failures in the APS can lead to high operational disruptions and maintenance costs. This dataset distinguishes between APS-related failures (positive class) and non-APS-related failures (negative class). The goal is to minimize false negatives, which could result in costly vehicle breakdowns.

Key Challenges:
Handling missing values in the dataset.
Minimizing false negatives due to their higher cost (500 units).
Focusing on accuracy instead of latency for optimal performance.
The model aims to predict APS failures accurately while reducing overall costs.

Solution Overview
This project uses machine learning to address APS failure prediction:
Data Preprocessing: Null values handled with imputation techniques such as SimpleImputer with constant values.
Cost-Sensitive Modeling: A model is designed to minimize false negatives (which have a higher cost).
Best Model: XGBoost Classifier was chosen after experimenting with multiple models, due to its robustness and cost-effective performance.

Installation
Clone the repository:
git clone https://github.com/maybemnv/predictive-maintenance-for-air-pressure-system-aps.git
cd aps-sensor-detection
Install dependencies:
pip install -r requirements.txt
To run the Flask API:
python app/app.py
For the Streamlit frontend (optional):
streamlit run frontend/streamlit_app.py

Model Evaluation
Best Model: XGBoost Classifier
Total Cost: 2950 units
Model Accuracy: 85%
Precision: 90%
Recall: 80%
This model effectively minimizes false negatives, leading to cost optimization.
Future Improvements
Hyperparameter Tuning: Further optimize model performance using techniques like grid search.
Real-Time Prediction: Integrate the model with real-time sensor data for continuous prediction.
Deployment: Host the model on cloud platforms like AWS or Heroku for broader accessibility.
License
This project is licensed under the MIT License - see the LICENSE file for details.

