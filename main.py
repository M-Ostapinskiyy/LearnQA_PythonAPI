import requests

print('Hello from Misha!')

response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)