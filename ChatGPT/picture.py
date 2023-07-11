import requests

KEY = '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'


def generate(message):
    url = 'https://api.openai.com/v1/images/generations'

    headers = {
        'Authorization': f'Bearer {KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json={"promt": message}, headers=headers)
    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error: ", response.text)


text = 'Buggatti and Volvo'
generate(text)
