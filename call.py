import requests
import json

def send_to_ocr():
    url = "http://127.0.0.1:8000/ocr"
    headers = {"Content-Type": "application/json, charset=utf-8"}
    data = {"image_path": "https://i.pinimg.com/736x/87/b1/a4/87b1a4a5078350c42c7f1a422464498d.jpg"}
    res = requests.post(url, headers=headers, data=json.dumps(data))

    print("Status Code", res.status_code)
    print("Response ", json.loads(res.text))

if __name__ == '__main__':
    send_to_ocr()