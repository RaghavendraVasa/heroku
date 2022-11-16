from datetime import timedelta
import pytest
import requests

url = 'https://restful-booker.herokuapp.com/booking'
param = {'firstname': 'Rahul', 'lastname': 'Vasa'}


@pytest.fixture(scope='module')
def fixture():
    print('\nStarting GET Test cases')
    yield
    print('\nExecuted GET Test cases')


@pytest.mark.get
def test_get_all_request(fixture):
    response = requests.get(url)
    assert response.status_code == 200
    assert response.elapsed < timedelta(seconds=2)


@pytest.mark.get
def test_get_filter_request(fixture):
    response = requests.get(url, params=param)
    assert response.status_code == 200
    assert response.elapsed < timedelta(seconds=2)
