import os  # Importing the os module for interacting with the operating system
import sys  # Importing the sys module for interacting with the Python runtime environment
import logging  # Importing the logging module to configure and use loggers

# Defining the format of log messages including timestamp, log level, module name, and the actual log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"  # Directory where log files will be stored
log_filepath = os.path.join(log_dir, "running_logs.log")  # Complete file path for the log file within the logs directory

# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configuring the basic logging settings
logging.basicConfig(
    level=logging.INFO,  # Setting the logging level to INFO, which means it will capture info, warning, error, and critical messages
    format=logging_str,  # Specifying the format for log messages

    # Defining handlers for logging: one for writing logs to a file, another for displaying them on the console
    handlers=[
        logging.FileHandler(log_filepath),  # Logging to the specified file
        logging.StreamHandler(sys.stdout)  # Logging to the console (standard output)
    ]
)

# Creating a logger object with a custom name to be used in the application
logger = logging.getLogger("ETEP_MLOps_MLflow_AWS_Logger")
