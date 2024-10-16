# Завдання 7
# Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль.
# Файл має містити такі стовпчики: імена, прізвища, дати народження та місто проживання.
# Реалізуйте можливості перезапису цього файлу, додавання нових рядків до наявного файлу,
# рядкового читання з файлу та конвертації всього вмісту у формати XML та JSON.
import csv
import json
import xml.etree.ElementTree as ET


def write_csv(filename, data, mode='w'):
    with open(filename, mode, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Surname', 'Birthdate', 'City'])
        writer.writerows(data)


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

