import requests
import json

from generate_token import generateToken


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)


def get_user_data(url, headers):
    response = requests.get(f"{url}", headers=headers)
    if response.status_code == 200:
        print("Successfully fetched the details")
        formatted_print(response.json())

    else:
        print(f"there's a {response.status_code} error with your request")


auth_token = generateToken("https://qa-nrp-api.laerdalblr.in/account/v1/token")
print("Token : ", auth_token)


class getUserById:

    def __init__(self, url):
        headers = {"content-type": "application/json", "Authorization": 'Bearer {}'.format(auth_token)}
        get_user_data(url, headers)


if __name__ == "__main__":
    apiCall = getUserById("https://qa-nrp-api.laerdalblr.in/org-user/v1/users/1214422")
