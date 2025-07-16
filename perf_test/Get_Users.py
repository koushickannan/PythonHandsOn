import json, time
import random

from locust import task, HttpUser, TaskSet, between, constant


def get_headers():
    token = 'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6IjEiLCJ1c2VySWQiOiIzIiwic3RvcmVDb2RlIjoiNzEwIiwibGFuZ0NvZGUiOiJlbiIsInVzZXJOYW1lIjoicm9zZU1hZXJ3eSIsInJvbGUiOiJ0ZW5hbnRfYWRtaW4iLCJyb2xlSWQiOjQ0NSwiZXh0ZXJuYWxVc2VySWQiOiIxMjMiLCJyZWdpb24iOiJVUyIsImV4cCI6MTY4MTM4MzM0NCwiaWF0IjoxNjgxMjk2OTQ0LCJpc3MiOiIxIiwic3ViIjoiMSJ9.bzkFzGLtCy9osLquE7Bin-W_aKRLguObbNS00yKBlfku5HWVgBRrrwImVP0I3pPSIFJZh-40wfdyAcD8kG1XzAuoRY4Pe1zUtjRgmfvQOI6GisgZjGRuMgvLNdtMcAGY8Ksb5L4qM4FnRAv-GBOm7rFEf3jWib_LMy__Tz6egVtMNV5EZH-uqevpONY9cjsrRcJ9hN93Pr9ppnmNowGXAhiisgnh2YwY6Pa9QkD0ESln0s5W_fI26XKcLGVsx464vPzjWatPScFK3QoUEdL8SsXCY_A_FPtBKxKtVyN2iRDVgWLUIaFEGfP7PbfJfgK6ip9QHRRKVjq0fumt7_leKQ'
    headers = {"content-type": "application/json", "Authorization": token}
    return headers


class WebsiteTestUser(HttpUser):
    wait_time = constant(0)

    # between(0.5, 1.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

        self.client.headers = get_headers()

    @task
    def getUsers(self):
        url: str = "/org-user/v1/users?query=(nrpId=isnull=0)&page-number=1&page-size=10"
        response = self.client.get(url)
        print("Status code is : " + str(response.status_code))
