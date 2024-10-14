# Завдання 8

# Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу 
# та словник як передавальні дані(опціональний).
# Виконувати запит з отриманим методом на отриманий ресурс, передаючи
# дані відповідним методом, та друкувати на консоль статус-код, заголовки та тіло відповіді.

import requests


def http_client(url, method, data=None):
    if method.upper() == 'GET':
        response = requests.get(url, params=data)
    elif method.upper() == 'POST':
        response = requests.post(url, json=data)
    elif method.upper() == 'PUT':
        response = requests.put(url, json=data)
    elif method.upper() == 'DELETE':
        response = requests.delete(url, json=data)
    else:
        print("Непідтримуваний метод.")
        return

    print(f"Статус-код: {response.status_code}")
    print("Заголовки:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    print("Тіло відповіді:")
    print(response.text)


url = "https://jsonplaceholder.typicode.com/posts/1"
http_client(url, "GET")

data = {"title": "new title", "body": "new body"}
http_client(url, "PUT", data)
