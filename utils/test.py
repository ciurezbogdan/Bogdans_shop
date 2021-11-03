import requests

response = requests.get('https://api.github.com', params={'q': 'requests+language:python'})
json_resp = response.text

print(json_resp)
