import requests
import json


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)
    email_id = obj['orgInfo']['userInfo']['emailId']
    print("Email ID is : ", email_id)


def get_payload():
    payload = {
        "userName": "victorymarsi",
        "password": "Pass@123",
        "remember": False
    }
    return payload


def get_user_data(url, headers):
    response = requests.post(f"{url}", headers=headers, json=(get_payload()))

    if response.status_code == 200:
        print("Successfully fetched the details")
        formatted_print(response.json())

    else:
        print(f"there's a {response.status_code} error with your request")


class loginBff:
    def __init__(self, url):
        token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6IjEiLCJ1c2VySWQiOiIxIiwic3RvcmVDb2RlIjoiNzEwIiwibGFuZ0NvZGUiOiJlbiIsInJvbGUiOiJndWVzdCIsInJvbGVJZCI6Mjg1LCJ1dWlkIjoiMjI2NjBjZGMtZGQzOS00MTUzLThhMjktMzNkMDk1MGU5NDUzIiwicmVnaW9uIjoiVVMiLCJleHAiOjk0NTk2Mjc3MTUsImlhdCI6MTY4MzYyNzcxNSwiaXNzIjoiMSIsInN1YiI6IjEifQ.WGeXcQTss7KZMacAKSmqBTs-T_1dInxrYNCep-rU72w'
        headers = {"content-type": "application/json", "Authorization": token}
        get_user_data(url, headers)


if __name__ == "__main__":
    apiCall = loginBff("https://dev-nrp-bff.laerdalblr.in/login")
