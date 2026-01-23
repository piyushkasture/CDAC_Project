import json

# @pytest.fixture(scope="session")
def test_data():
    with open("testData/login_test_data.json", "r", encoding="utf-8") as file:
        # return json.load(file)
        data = json.load(file)

    usernames = data["username"]
    passwords = data["password"]

    #create combinations
    test_dataa = []
    for username in usernames:
        for password in passwords:
            test_dataa.append((username, password))

    return test_dataa