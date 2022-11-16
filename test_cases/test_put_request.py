import json
import pytest
import requests
import test_auth_request
import test_post_request

url = 'https://restful-booker.herokuapp.com/booking/' + str(test_post_request.booking_id)
header_data = {'Cookie': 'token=' + str(test_auth_request.token)}


@pytest.mark.put
def test_put_request():
    file = open('./json/update_booking.json', mode='r')
    request_json = json.loads(file.read())
    print(request_json)
    response = requests.put(url, json=request_json, headers=header_data)
    print(response.text)
    print(response.status_code)
