
# 카카오 메세지
import os
import json
import requests
import config

def sendToMeMessage(text):
    KAKAO_TOKEN = config.KAKAO_TOKEN # 카카오 REST API KEY
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

   
# 카톡으로 결과 전송
text = "Hello, This is KaKao Message Test!!("+os.path.basename(__file__).replace(".py", ")")
print(sendToMeMessage(text).text)
