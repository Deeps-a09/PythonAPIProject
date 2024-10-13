import pytest
import allure
import requests

# Positive test case
@allure.title("GET Request with positive ID")
@allure.description("TC#1 -> Verify that GET Request with positive ID")
@allure.tag("regression", "p0", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Deepshikha Arya")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_positive_id():
    url = "https://restful-booker.herokuapp.com/booking/2"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 200

# Negative test case
@allure.title("GET Request with negative ID")
@allure.description("TC#2 -> Verify that GET Request with negative ID")
@allure.label("owner", "Deepshikha Arya")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_negative_id():
    url = "https://restful-booker.herokuapp.com/booking/-2"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 404

# Negative test case
@allure.title("GET Request with invalid ID")
@allure.description("TC#3 -> Verify that GET Request with invalid ID")
@allure.tag("regression", "p0", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Deepshikha Arya")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_invalid_id():
    url = "https://restful-booker.herokuapp.com/booking/abc"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 404

# Failed test case
@allure.title("GET Request with existing ID")
@allure.description("TC#3 -> Verify that GET Request with existing ID")
@allure.tag("regression", "p0", "smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Deepshikha Arya")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_single_request_by_existing_id():
    url = "https://restful-booker.herokuapp.com/booking/abc"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 200



