import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects= True)

response_history = len(response.history)
last_url = response

print(response_history)
print(last_url.url)


