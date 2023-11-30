"""
Author: Mohamed Yasser
Date: Nov, 2023
This script used for testing types and ranges
"""

import great_expectations as ge
def test_columns_exist(data: ge.dataset.PandasDataset):
    expected_columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                        'hours-per-week', 'native-country', 'salary']
    for column in expected_columns:
        assert data.expect_column_to_exist(column)['success'], f"{column} does not exist"


def test_column_dtypes(data: ge.dataset.PandasDataset):
    expected_column_types = {
        'age': 'int64',
        'workclass': 'object',
        'fnlwgt': 'int64',
        'education': 'object',
        'education-num': 'int64',
        'marital-status': 'object',
        'occupation': 'object',
        'relationship': 'object',
        'race': 'object',
        'sex': 'object',
        'capital-gain': 'int64',
        'capital-loss': 'int64',
        'hours-per-week': 'int64',
        'native-country': 'object',
        'salary': 'object'}
    for column, dtype in expected_column_types.items():
        assert data.expect_column_values_to_be_of_type(
            column, dtype)['success'], f"{column} should be of type {dtype}"


def test_education_num_column(data: ge.dataset.PandasDataset):
    assert data.expect_column_values_to_be_between('education-num', 1, 17)[
        'success'], "education_num column includes unknown category"

def test_hours_per_week_range(data: ge.dataset.PandasDataset):
    assert data.expect_column_values_to_be_between('hours-per-week', 1, 99)[
        'success'], "hours_per_week column is not within range of 1 and 99"
