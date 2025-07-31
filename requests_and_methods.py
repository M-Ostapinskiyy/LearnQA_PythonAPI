import requests

# 1. http-запрос любого типа без параметра method
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response1.status_code)
print(response1.text)

#2. http-запрос не из списка. Например, HEAD
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response2.status_code)
print(response2.text)

#3. запрос с правильным значением method
payload = {"method": "GET"}

response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params= payload)

print(response3.status_code)
print(response3.text)

#4
methods = ["GET", "POST", "PATCH", "PUT", "DELETE", "HEAD"]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
results = {}
for http_method in ["GET", "POST", "PATCH", "PUT", "DELETE", "HEAD"]:
    for method_value in methods:
        payload = {}
        if http_method == 'GET':
            payload = {'method': method_value}
        else:
            payload = {'method': method_value}
# Отправка запроса с указанными параметрами
response = requests.request(method=http_method, url=url, params=payload, data=payload)

# Формирование ключа для хранения результата, включающего HTTP-метод и значение method
key = f"{http_method}|{method_value}"
results[key] = {
    "status_code": response.status_code,
    "http_method": http_method,
    "method_value": method_value,
    "text": response.text
        }

# Вывод результатов для анализа
print("Результаты запросов:")
for key, data in results.items():
    print(f"\n{key}:")
    print(f"  HTTP-метод: {data['http_method']}")
    print(f"  Значение параметра method: {data['method_value']}")
    print(f"  Код ответа: {data['status_code']}")
    print("  Ответ сервера:")
    print(data['text'])