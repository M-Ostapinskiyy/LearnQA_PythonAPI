from http.client import responses
from json.decoder import JSONDecodeError
import requests

# response = requests.get("https://playground.learnqa.ru/api/hello", params = {"name": "User "})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])
#
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")

#Проверка типа запроса и параметров

# response = requests.get("https://playground.learnqa.ru/api/check_type")
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/check_type", params = {"param1": "value1"}) #params используется для GET
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/check_type", data = {"param1": "value1"}) #data используется для POST
# print(response.text)

#Коды ответа сервера

# response = requests.post("https://playground.learnqa.ru/api/check_type") #проверяем код ответа 200
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_500") #проверяем код ответа 500
# print(response.status_code)
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/something") #проверяем код ответа 404
# print(response.status_code)
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True) #проверяем код ответа 301 allow_redirects=False/True позволяет следовать до конечной точки редиректа
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)

#Заголовки

# headers = {"some_headers": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
# print(response.text) #headers requst
# print(response.headers) #header response

#Cookie

# payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)
# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))
#
# print(response.headers)

#Учимся передавать полученый Cookie

payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
#
# cookies = {'auth_cookie': cookie_value}
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)
#
# print(response2.text)

#Напишем код, который работает одновременно с правильным и неправильным логином и паролем

response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)

cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response2.text)

