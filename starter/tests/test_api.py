"""
Author: Mohamed Yasser
Date: Nov, 2023
This script used for testing api
"""

import requests
import json
import pandas as pd
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture()
def data_low():
    df = pd.read_csv("data/clean.csv")
    test = df.drop('salary', axis=1).iloc[0].to_dict()
    return test
@pytest.fixture()
def data_high():
    df = pd.read_csv("data/clean.csv")
    test = df.drop('salary', axis=1).iloc[9].to_dict()
    return test


def test_get_data():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Welcome to the MLops Project 3 API! \
Please use docs to see the API documentation."}

def test_post_data_success(data_low):
    data = json.dumps(data_low)
    r = client.post("/predict/", data=data)
    assert r.status_code == 200


def test_post_data_fail():
    data = {"age": -5, "feature_2": "test string"}
    r = client.post("/predict/", data=json.dumps(data))
    assert r.status_code == 422


def test_post_low(data_low):
    data = json.dumps(data_low)
    r = client.post("/predict/", data=data)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == '<=50K'

def test_post_high(data_high):
    data = json.dumps(data_high)
    r = client.post("/predict/", data=data)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == '>50K'



# import pytest
# from http import HTTPStatus
# from fastapi.testclient import TestClient
# import sys 
# sys.path.append("./")
# from starter.app.main import app

# client = TestClient(app)


# def assert_response(response, expected_status, expected_method):
#     assert response.status_code == expected_status
#     assert response.request.method == expected_method


# def test_greetings():
#     response = client.get('/')
#     assert_response(response, HTTPStatus.OK, "GET")
#     assert response.json() == "Hello Geeks"


# @pytest.mark.parametrize('test_input, expected', [
#     ('age', "Age of the person - numerical - int"),
#     ('fnlwgt', 'MORE INFO NEEDED - numerical - int'),
#     ('race', 'Race of the person - nominal categorical - str')
# ])
# def test_feature_info(test_input: str, expected: str):
#     response = client.get(f'/feature_info/{test_input}')
#     assert_response(response, HTTPStatus.OK, "GET")
#     assert response.json() == expected


# def test_predict():
#     data = {
#         'age': 38,
#         'workclass': "state-gov",
#         'education': "bachelors",
#         'maritalstatus': "never-married",
#         'occupation': "adm-clerical",
#         'relationship': "not-in-family",
#         'race': "white",
#         'sex': "male",
#         'nativecountry': "united-states",
#         'fnlwgt': 15,
#         'educationnum': 1,
#         'capitalgain': 0,
#         'capitalloss': 0,
#         'hoursperweek': 5,

#     }
#     response = client.post("/predict/", json=data)
#     assert_response(response, HTTPStatus.OK, "POST")
#     assert 0 <= response.json()['label'] <= 1
#     assert response.json()['salary'] in ['>50k', '<=50k']


# def test_missing_feature_predict():
#     data = {"age": 0}
#     response = client.post("/predict/", json=data)
#     assert_response(response, HTTPStatus.UNPROCESSABLE_ENTITY, "POST")
#     assert response.json()["detail"][0]["type"] == "value_error.missing"
