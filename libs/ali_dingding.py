import requests
import json


def   send_code(msg):
    head = {
        "Content-Type":"application/json"
    }
    datas = json.dumps({"msgtype": "text",
            "text": {"content":msg}
            })
    da = requests.post("https://oapi.dingtalk.com/robot/send?access_token=63c1fb489a694021dca90cf0bff5e024f45b8e869e5dffc7a3b00f3ad1a9a8e5", headers=head, data=datas)
    print(da.text)
