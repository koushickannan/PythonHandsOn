import json
import random

from locust import task, HttpUser, TaskSet, between


def get_headers():
    token = 'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6IjEiLCJ1c2VySWQiOiIzIiwic3RvcmVDb2RlIjoiNzEwIiwibGFuZ0NvZGUiOiJlbiIsInVzZXJOYW1lIjoicm9zZU1hZXJ3eSIsInJvbGUiOiJ0ZW5hbnRfYWRtaW4iLCJyb2xlSWQiOjQ0NSwiZXh0ZXJuYWxVc2VySWQiOiIxMjMiLCJyZWdpb24iOiJVUyIsImV4cCI6MTY4MTc5MzE1MCwiaWF0IjoxNjgxNzA2NzUwLCJpc3MiOiIxIiwic3ViIjoiMSJ9.3ISyx7cT0cBRzKqKzesbCzAn_DOTIs8xkALnrxJmlAT_w9H6tXvX7aFIRQHhY_u5CNKKYh-OWruA7TOMzjCoT4PueNkzMOqKwLutMaYslVcyuv_s-xyhqxY3E3KrCjjMpx6f0FnghRdSuhdBze1m4F4Fjm91LsVYvnU6ZLibcqypDt3nRLgBxaSyQS8nwyQWA_Q1bhXiF7gMm22Rxtr2MB3YQawSZmLuiFCA7OdEExxxUOyIcyYSAvIB6O-9fvTbx3mnqX1iizwbV-KQNJJlvjDhvqLLOG00YbrY4lNnL15a0o4Ahdh_8WQ6KOoXd5ipMeMK8ThK-OGZ3mZ28gxIDw'
    headers = {"content-type": "application/json", "Authorization": token}
    return headers


def get_payload():
    number = random.randint(500, 99999)
    num = str(number)

    emailAddress = "George.Addams" + num + "@mailinator.com"

    payload = {"user": {"firstName": "Steve", "lastName": "Rogers", "emailId": emailAddress, "timeZoneId": 1,
                        "hrisId": "9843" + num, "region": "US",
                        "unit": [{"unitId": 8082, "statusId": 2, "jobId": 4444}]}}
    return payload


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 1.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

        self.client.headers = get_headers()

    @task
    def createOrgUser(self):
        url: str = "/org-user/v1/organizations/4559/users?selfRegister=false"

        response = self.client.post(url, json.dumps(get_payload()))

        print("Status code is : " + str(response.status_code))
