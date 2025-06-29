import json

def load_login_data(path="data/login_data.json"):
    """
    Load login test data from a JSON file.

    Args:
        path (str): Path to the JSON file containing login credentials.
                    Default is 'data/login_data.json'.

    Returns:
        list[dict]: A list of dictionaries, each representing one set of login credentials.

    Example JSON format:
    [
        { "username": "user1", "password": "pass1" },
        { "username": "user2", "password": "pass2" }
    ]
    """
    with open(path, "r") as fileContent:
        return json.load(fileContent)