import json
import jsonpath
import pytest
import requests

url = 'https://restful-booker.herokuapp.com/auth'
token = None


@pytest.mark.auth
def test_auth_request():
    global token
    file = open('./json/auth.json', mode='r')
    request_json = json.loads(file.read())
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    token = jsonpath.jsonpath(response_json, 'token')[0]
    print('Token is : ' + token)
