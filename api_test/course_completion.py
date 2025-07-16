import json
import requests
from faker import Faker


def formatted_print(obj):
    text = json.dumps(obj, indent=4)
    print(text)


def get_headers():
    headers = {"content-type": "application/xml"}
    return headers


def get_payload(source_id):
    payload = f'''<?xml version="1.0" encoding="UTF-8"?>
<imsx_POXEnvelopeRequest xmlns="http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0">
   <imsx_POXHeader>
      <imsx_POXRequestHeaderInfo>
         <imsx_version>V1.0</imsx_version>
         <imsx_messageIdentifier>5eb98ff010e35</imsx_messageIdentifier>
      </imsx_POXRequestHeaderInfo>
   </imsx_POXHeader>
   <imsx_POXBody>
      <replaceResultRequest>
         <resultRecord>
            <sourcedGUID>
               <sourcedId>{source_id}</sourcedId>
            </sourcedGUID>
            <result>
               <resultScore>
                  <language>en-US</language>
                  <textString>1</textString>
               </resultScore>
            </result>
         </resultRecord>
      </replaceResultRequest>
   </imsx_POXBody>
</imsx_POXEnvelopeRequest>'''

    print("payload : ", payload)
    return payload


# def course_completion(url, headers, source_id):
#     response = requests.post(f"{url}", headers=get_headers(), data=get_payload(source_id))
#     if response.status_code == 200:
#         print("Successfully completed the topic")
#         ##formatted_print(response.json())
#
#     else:
#         print(f"there's a {response.status_code} error with your request")
#         ##formatted_print(response.json())


class CourseCompletion:
    def __init__(self, url, source_id):
        response = requests.post(f"{url}", headers=get_headers(), data=get_payload(source_id))
        if response.status_code == 200:
            print("Successfully completed the topic")
            print(f"Response :", response.content)

        else:
            print(f"there's a {response.status_code} error with your request")


if __name__ == "__main__":
    apiCall = CourseCompletion(
        "https://cs3n-test.contentservice.net/op_lis_endpoint",
        "6FE28199-0C18-EF11-96F5-000D3AA5C1C7|precourse-self-assessment|1714501800000|253402300738999")
