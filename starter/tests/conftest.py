"""
Author: Mohamed Yasser
Date: novamber, 2023
This script holds the conftest data used with pytest module
"""
import os
import pytest
import pandas as pd
import great_expectations as ge


@pytest.fixture(scope='session')
def data():
    """
    Data loaded from csv file used for tests

    Returns:
        df (ge.DataFrame): Data loaded from csv file
    """
    file_path = './data/clean.csv'
    if not os.path.exists(file_path):
        pytest.fail(f"Data not found at path")
    df = pd.read_csv(file_path)
    df = ge.from_pandas(df)

    return df
