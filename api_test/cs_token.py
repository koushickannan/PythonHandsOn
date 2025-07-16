import base64
import json
import requests
from faker import Faker


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)

def basic_auth_token():
    username = "cdp_exemplar_qa-common-rqi"
    password = "2UMcbJMtwfXvbRT8RFTSaTz5PqSZnLgTZ6QxWgNxWZKJExqm"   
    credentials = f"{username}:{password}"
    # Encode the credentials in Base64
    auth_token = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    print("basic auth token : ", auth_token)  
    return auth_token

def get_headers():
   
    headers = {"content-type": "application/json", "Authorization": 'Basic {}'.format(basic_auth_token()) }
    return headers

def create_token(url, headers):
    auth = ()
    response = requests.post(f"{url}", headers=headers, json=({"org":"40022193"}))
    if response.status_code == 200:
        print("Successfully fetched the details :", response.json()['accessToken'])
        #formatted_print(response.json())
        

    else:
        print(f"there's a {response.status_code} error with your request")
        formatted_print(response.json())


class token_gen:
    def __init__(self, url):
        create_token(url, get_headers())


if __name__ == "__main__":
    apiCall = token_gen("https://auth-test.contentservice.net/v1/token")
