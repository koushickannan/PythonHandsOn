import base64
import json
import requests
from faker import Faker


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)

def get_headers():
   
    headers = {"content-type": "application/json" }
    return headers

def generate_form_data():
    form_data_body = {}
    form_data_body["launch_url"] = 'https://cs3n-staging.contentservice.net/launch_lti?manifest=manifest/rqi_provider_2025_aha_moc_entry_test&launch_as=learner'
    form_data_body['oauth_consumer_key'] = '4f468578-8ca8-44bb-8aa1-fd513881884a|4p3z7-hdtgb-8r2sq'
    form_data_body['oauth_consumer_secret'] = 'a58f91e412b311e1'
    form_data_body['custom_org_unit_id']  = 26550
    form_data_body['custom_organization_id'] = 2000984
    form_data_body['custom_organization_name'] = 'Test_PI7.3_systemteam_Cachetest_Dontuse_MohanR'
    form_data_body['XXcustom_institution_id'] = 17
    print(form_data_body)

    return form_data_body

def generate_lti_body(url, headers):   
    response = requests.post(f"{url}", headers=headers, data=generate_form_data())
    if response.status_code == 200:
        print("Successfully fetched the details :", response.json()['accessToken'])
        #formatted_print(response.json())
        

    else:
        print(f"there's a {response.status_code} error with your request")
        formatted_print(response.json())



class launch_lti:
    def __init__(self, url):
        generate_lti_body(url, get_headers())


if __name__ == "__main__":
    apiCall = launch_lti()