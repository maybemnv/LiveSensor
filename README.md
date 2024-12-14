# APS Sensor Detection: Predictive Maintenance Model
#123

## Problem Statement
The **Air Pressure System (APS)** in heavy-duty vehicles is crucial for essential functions like braking. APS failures can lead to operational disruptions and high maintenance costs. This dataset categorizes failures into APS-related (positive class) and non-APS-related (negative class) failures. The goal is to minimize false negatives, as these result in costly vehicle breakdowns.

### Key Challenges:
- Handling missing values.
- Minimizing false negatives (high cost: 500 units).
- Focusing on accuracy rather than latency.

## Solution Overview
This project uses machine learning to predict APS failures:

- **Data Preprocessing**: Null values handled using imputation techniques like **SimpleImputer** with constant values.
- **Cost-Sensitive Modeling**: Focuses on minimizing false negatives, which are more costly.
- **Best Model**: **XGBoost Classifier** was selected after experimenting with several models for its robust and cost-effective performance.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maybemnv/predictive-maintenance-for-air-pressure-system-aps.git
   cd aps-sensor-detectionn
2. Install dependicies:
   ```bash
      pip install -r requirements.txt
3. To run the Flask API:
   ```bash
    python app/app.py
## Model Evaluation

### Best Model: XGBoost Classifier
- **Total Cost**: 2950 units
- **Accuracy**: 85%
- **Precision**: 90%
- **Recall**: 80%

The XGBoost Classifier effectively minimizes false negatives, leading to a significant cost reduction.

## Future Improvements
- **Hyperparameter Tuning**: Perform further optimization using grid search or randomized search to improve model performance.
- **Real-Time Prediction**: Integrate with real-time sensor data to predict failures in real-time.
- **Deployment**: Host the model on cloud platforms like AWS or Heroku to enable access from various devices and enhance scalability.
