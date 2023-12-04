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
from app.main import app

client = TestClient(app)

def convert_names(data):
    replace_names = ["education-num", "marital-status", "capital-gain", "hours-per-week", "native-country"]
    new_names = ["educationnum", "maritalstatus", "capitalgain", "hoursperweek", "nativecountry" ]
    for old_name, new_name in zip(replace_names, new_names):
        if old_name in data:
            data[new_name] = data.pop(old_name)
    return data

    
@pytest.fixture()
def data_low():
    df = pd.read_csv("data/clean.csv")
    test = df.drop('salary', axis=1).iloc[0].to_dict()
    
    return convert_names(test)
    
@pytest.fixture()
def data_high():
    df = pd.read_csv("data/clean.csv")
    test = df.drop('salary', axis=1).iloc[9].to_dict()
    return convert_names(test)


def test_get_data():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == "Hello Geeks"


def test_post_data_success(data_low):
    data = json.dumps(data_low)
    r = client.post("/predict/", data=data)
    assert r.status_code == 422


def test_post_data_fail():
    data = {"age": -5, "feature_2": "test string"}
    r = client.post("/predict/", data=json.dumps(data))
    assert r.status_code == 422


def test_post_low(data_low):
    data = json.dumps(data_low)
    r = client.post("/predict/", data=data)
    print(r.json())
    assert r.status_code == 422
    assert r.json()['salary']  == '<=50K'

def test_post_high(data_high):
    data = json.dumps(data_high)
    r = client.post("/predict/", data=data)
    print(r.json())
    assert r.status_code == 422
    assert r.json()['salary']  == '>50K'

