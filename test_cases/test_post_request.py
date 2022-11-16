import json
import jsonpath
import pytest
import requests

url = 'https://restful-booker.herokuapp.com/booking'
header_data = {'Content-Type': 'application/json', 'Accept': 'application/json'}
booking_id = None


@pytest.mark.post
def test_post_request():
    global booking_id
    file = open('./json/create_booking.json', mode='r')
    request_json = json.loads(file.read())
    print(request_json)
    response = requests.post(url, json=request_json)
    print(response.text)
    print(response.status_code)
    response_json = json.loads(response.text)
    booking_id = jsonpath.jsonpath(response_json, 'bookingid')[0]
    print(booking_id)
