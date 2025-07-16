import json
import random

from locust import task, HttpUser, TaskSet, between, constant


def get_headers():
    token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6IjEiLCJ1c2VySWQiOiIxIiwic3RvcmVDb2RlIjoiNzEwIiwibGFuZ0NvZGUiOiJlbiIsInJvbGUiOiJndWVzdCIsInJvbGVJZCI6Mjg1LCJ1dWlkIjoiMjI2NjBjZGMtZGQzOS00MTUzLThhMjktMzNkMDk1MGU5NDUzIiwicmVnaW9uIjoiVVMiLCJleHAiOjk0NTk2Mjc3MTUsImlhdCI6MTY4MzYyNzcxNSwiaXNzIjoiMSIsInN1YiI6IjEifQ.WGeXcQTss7KZMacAKSmqBTs-T_1dInxrYNCep-rU72w'
    headers = {"content-type": "application/json", "Authorization": token}
    return headers


def get_payload():

    payload = {
        "userName": "victorymarsi",
        "password": "Pass@123",
        "remember": False
    }
    return payload


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 1.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

        self.client.headers = get_headers()

    @task
    def createOrgUser(self):
        url: str = "/login"

        response = self.client.post(url, json.dumps(get_payload()))

        print("Status code is : " + str(response.status_code))
