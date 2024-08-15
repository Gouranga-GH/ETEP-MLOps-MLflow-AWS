import os  # For interacting with the operating system, such as file operations
from src.ETEP_MLOps_MLflow_AWS.utils import logger  # Importing a logger utility
from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data
import pandas as pd  # Importing pandas for data manipulation
from src.ETEP_MLOps_MLflow_AWS.entity.config_entity import DataTransformationConfig  # Importing DataTransformationConfig class

# Definition of the DataTransformation class
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        # Initializing the class with a DataTransformationConfig object
        self.config = config

    # Note: You can add different data transformation techniques such as scaling or PCA here.
    # This class can also be used for Exploratory Data Analysis (EDA) before passing the data to the model.

    # Method to split the data into training and test sets
    def train_test_spliting(self):
        # Load the dataset from the path specified in the configuration
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets (75% train, 25% test)
        train, test = train_test_split(data)

        # Save the split datasets to CSV files in the root directory specified in the configuration
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Log the shapes of the training and test sets
        logger.info("Split data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        # Print the shapes of the training and test sets to the console
        print(train.shape)
        print(test.shape)
