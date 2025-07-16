import json

import requests


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)
    global current_token
    current_token = obj['data']['token']
    print("tokenGeneration : ", current_token)    


def get_headers():
    token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6IjEiLCJ1c2VySWQiOiIyMjMiLCJzdG9yZUNvZGUiOiI3MTAiLCJsYW5nQ29kZSI6ImVuIiwicm9sZSI6InRlbmFudF9hZG1pbiIsInJvbGVJZCI6NDQ1LCJleHRlcm5hbFVzZXJJZCI6IjEiLCJyZWdpb24iOiJVUyIsImV4cCI6MTY4MzcxNjczOSwiaWF0IjoxNjgzNjMwMzM5LCJpc3MiOiIxIiwic3ViIjoiMSJ9.vggd9ifbXt5e9QnppfRxuxi9hgGo4tBlrjlVHQiJBK0'
    headers = {"content-type": "application/json", "Authorization": token}
    return headers


def get_payload():
    payload = {"tenantId": "1", "tenantSecret": "651c0b1373527e43a46d26300dd94f022f297578223f89f69ded529289d8dafe",
               "grantType": "oauth2.0",
               "scope": {"role": "tenant_admin", "userId": "223", "storeCode": "710", "langCode": "en",
                         "externalUserId": "1", "region": "US"}}
    # formatted_print(payload)
    return payload


def generateToken(url):
    response = requests.post(f"{url}", headers={"content-type": "application/json"}, json=(get_payload()))
    if response.status_code == 200:
        print("Successfully fetched the details")
        formatted_print(response.json())

    else:
        print(f"there's a {response.status_code} error with your request")

    return response.json()['data']['token']


""" class generate_token:
    def __init__(self, url):
        generateToken(url, get_headers())


if __name__ == "__main__":
    apiCall = generate_token("https://dev-nrp-api.laerdalblr.in/account/v1/token") """
