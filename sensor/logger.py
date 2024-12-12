import logging
import os
from datetime import datetime

# Setting up the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory to store logs
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Defining the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO )