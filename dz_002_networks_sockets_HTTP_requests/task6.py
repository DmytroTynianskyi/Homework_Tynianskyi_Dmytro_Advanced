# Завдання 6

# Використовуючи сервіс https://jsonplaceholder.typicode.com /,
# спробуйте побудувати різні типи запитів та обробити відповіді.
# Необхідно попрактикуватися з urllib та бібліотекою requests.
# Рекомендується спочатку спробувати виконати запити, використовуючи urllib,
# а потім спробувати реалізувати те саме, використовуючи requests.

import requests
import urllib.request
import urllib.parse
import json

def urllib_get_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = urllib.request.urlopen(url)
    data = response.read()
    print("GET-запит (urllib):")
    print(json.loads(data))

def urllib_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"title": "foo", "body": "bar",
                      "userId": 1}).encode('utf-8')
    req = urllib.request.Request(
        url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    result = json.loads(response.read())
    print("POST-запит (urllib):")
    print(result)


urllib_get_request()
urllib_post_request()


# ----------------------------------------------------------------------------------------

def requests_get_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("GET-запит (requests):")
    print(response.json())


def requests_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=data)
    print("POST-запит (requests):")
    print(response.json())


requests_get_request()
requests_post_request()
