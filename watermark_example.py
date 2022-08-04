import json
import base64
import requests
from PIL import Image
from io import BytesIO

URL = "https://ec2-3-36-136-231.ap-northeast-2.compute.amazonaws.com/watermark"
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJleHAiOjE2OTA5OTE1NTZ9.HP4ZSmg_fQyl8Lcv1' \
        '-Z41RTZMhAHjTWwOJxPwlgpdeU '


def main():
    with open('sample_image.png', 'rb') as img:
        base64_string = base64.b64encode(img.read()).decode('utf-8')

    payload = json.dumps({
        "img": base64_string,
        "text": "DeepNatural. Inc",
        "size": 20
    })
    headers = {
        'Authorization': f'bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.post(URL, headers=headers, data=payload)
    img = Image.open(BytesIO(response.content))
    img.save("sample_image_watermark.png")


if __name__ == '__main__':
    main()
