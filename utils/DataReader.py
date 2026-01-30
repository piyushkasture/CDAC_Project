import json
import os

def data():
    # Open and read the JSON test data file
    with open("testdata/login_test_data.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)

    # Initialize empty list to store login test data
    login_data = []

    # Extract username, password, and validity from each test case
    for loginData in json_data:
        login_data.append((loginData["username"], loginData["password"], loginData["validity"]))

    return login_data


def get_valid_login():
    file_path = os.path.join("testdata", "admin_test_data.json")

    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    return json_data["valid_admin"]["username"], json_data["valid_admin"]["password"]
