import json

# @pytest.fixture(scope="session")
def data():
    with open("testdata/login_test_data.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)

    login_data =[]

    for loginData in json_data:
        login_data.append((loginData["username"], loginData["password"], loginData["validity"]))

    return login_data