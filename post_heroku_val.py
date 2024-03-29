import requests

data = {
        'age': 38,
        'workclass': "state-gov",
        'education': "bachelors",
        'maritalstatus': "never-married",
        'occupation': "adm-clerical",
        'relationship': "not-in-family",
        'race': "white",
        'sex': "male",
        'nativecountry': "united-states",
        'fnlwgt': 15,
        'educationnum': 1,
        'capitalgain': 0,
        'capitalloss': 0,
        'hoursperweek': 5,

    }


# POST request
response = requests.post('https://census-project-heroku-e79fa8f445c1.herokuapp.com/predict/', json=data)
print("Response code: ", response.status_code)
print("Response body: ", response.json())
