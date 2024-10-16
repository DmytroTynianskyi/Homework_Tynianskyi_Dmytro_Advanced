# Завдання 1
# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.
import json

data = {
    "name": "Ivan",
    "age": 25,
    "city": "Kyiv"
}

json_data = json.dumps(data)

with open('data.json', 'w') as file:
    file.write(json_data)

with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)
