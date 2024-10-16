# Завдання 4
# Створіть таблицю «матеріали» з таких полів: ідентифікатор,
# вага, висота та додаткові характеристики матеріалу.
# Поле «додаткові  характеристики матеріалу» має зберігати 
# у собі масив, кожен елемент якого є кортежем із двох значень:
# перше – назва характеристики, а друге – її значення.
import sqlite3

conn = sqlite3.connect('materials.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    weight INTEGER,
    height INTEGER,
    characteristics TEXT
)
''')

characteristics = [('color', 'red'), ('strength', 'high')]
cursor.execute('''
INSERT INTO materials (weight, height, characteristics) 
VALUES (?, ?, ?)
''', (100, 200, str(characteristics)))

conn.commit()

cursor.execute('SELECT * FROM materials')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

# Завдання 5
# Для таблиці «матеріалу» з завдання 4 створіть користувальницьку
# агрегатну функцію, яка рахує середнє значення ваги всіх матеріалів вислідної вибірки й округляє значення до цілого.


def average_weight(materials):
    total_weight = sum([material['weight'] for material in materials])
    avg_weight = total_weight / len(materials)
    return round(avg_weight)


materials = [
    {'weight': 100, 'height': 200},
    {'weight': 200, 'height': 150}
]
print(average_weight(materials))



# Завдання 6
# Для таблиці «матеріалу» з завдання 4 створіть функцію користувача,
# яка приймає необмежену кількість полів і повертає їх конкатенацію.

def concatenate_fields(*fields):
    return ''.join(fields)


print(concatenate_fields('weight', 'height', 'material'))



