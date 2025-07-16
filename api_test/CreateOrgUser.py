import json
import requests
from faker import Faker


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)


def get_headers():
    token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6IjEiLCJ1c2VySWQiOiIyMjMiLCJzdG9yZUNvZGUiOiI3MTAiLCJsYW5nQ29kZSI6ImVuIiwicm9sZSI6InRlbmFudF9hZG1pbiIsInJvbGVJZCI6NDQ1LCJleHRlcm5hbFVzZXJJZCI6IjEiLCJyZWdpb24iOiJVUyIsImV4cCI6MTY4MzcxNjczOSwiaWF0IjoxNjgzNjMwMzM5LCJpc3MiOiIxIiwic3ViIjoiMSJ9.vggd9ifbXt5e9QnppfRxuxi9hgGo4tBlrjlVHQiJBK0'
    headers = {"content-type": "application/json", "Authorization": token}
    return headers


def get_payload():
    fake = Faker()
    rand_num = str(fake.unique.random_int(min=1, max=999999))
    emailId = fake.first_name() + "." + fake.last_name() + rand_num + "@mailinator.com"
    print("Email Address : ", emailId)
    payload = {"user": {"firstName": "Steve", "lastName": "Rogers", "emailId": emailId, "timeZoneId": 1,
                        "hrisId": "9843" + rand_num, "region": "US",
                        "unit": [{"unitId": 10, "statusId": 2, "jobId": 11}]}}
    formatted_print(payload)
    return payload


def create_user(url, headers):
    response = requests.post(f"{url}", headers=headers, json=(get_payload()))
    if response.status_code == 200:
        print("Successfully fetched the details")
        formatted_print(response.json())

    else:
        print(f"there's a {response.status_code} error with your request")


class create_org_users:
    def __init__(self, url):
        create_user(url, get_headers())


if __name__ == "__main__":
    apiCall = create_org_users("https://dev-nrp-api.laerdalblr.in/org-user/v1/organizations/1/users?selfRegister=false")
