from sensor.exception import SensorException
import os 
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

if __name__=="__main__":
    file_path="C:\\Users\\MANAV\\Desktop\\codes\\predictive-maintenance-for-air-pressure-system-aps\\aps_failure_training_set1.csv"
    database_name="MNV"
    collection_name="APS"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)