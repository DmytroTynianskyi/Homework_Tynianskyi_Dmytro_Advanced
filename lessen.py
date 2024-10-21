# Створіть програму керування персоналом для збереження данних використовуйте sqlite3
# має бути можливість додавати персонал. В кожного робітника є наступні поля: Прізвище,
# Ім'я, зарплатня, Конверсія.
# 
# Створіть можливість отримати всіх робітників де виводьте
# їх імена прізвища та ІД.
# 
# Є можливість видалити робітника користувач вводить ІД
# робітника та він видаляється.
# 
# Є можливість отримати робітника по ІД де дізнатись
# більш детальну інформацію про нього а не тільки ім'я та прізвище.
# 
# Є можливість 
# порахувати зарплатню робітника для цього користувач вводить ІД робітника та отримує
# його зарплатню якщо конверсія більше 0.5 то до зарплатні нараховується бонус 10 відсотків.

# Додаткові задачі: Створіть можлдивість отримати зарплатні всіх робітників разом з бонусами
# якщо вони заслуговують на це та порахуйте суму всіх ЗП. Зробіть можливість пошуку за
# прізвищем робітника користувач вводить частину прізвища виведіть всі знайдені співпадіння з іх Ім'я прізвищем та ІД

import sqlite3

conn = sqlite3.connect('personnel.db')
cursor = conn.cursor()

def create_table_personnel():
    query ='''
    CREATE TABLE IF NOT EXISTS personnel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    salary REAL NOT NULL,
    conversion REAL NOT NULL
    );
    '''

conn.commit()

def add_personn():
    query = '''
    INSERT INTO personnel (last_name,first_name,salary,conversion)(?,?,?);
    '''
    cursor.execute(query, [last_name, first_name,salary,conversion])
    conn.commit()

def get_all_personnel():
    query = "SELECT last_name,first_name FROM personnel"
    result = cursor.execute(query)
    return result.fetchall()

def get_personn(id:int):
    query = '''
    "SELECT * FROM personnel
    WHERE id = ?
    '''
    result = cursor.execute(query,[id])
    return result.fetchall()
    

def delet_personn(id: int):
    query = """
    DELETE FROM personnel WHERE id = ?
    """
    result = cursor.execute(query, [id])
    conn.commit()
    

def calculate_salary_with_bonus(id):
    query = "SELECT salary, conversion FROM personnel WHERE id = ?;"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result:
        salary, conversion = result
        if conversion > 0.5:
            salary += salary * 0.1
            


    create_table_personnel() 
while True:
        choice = input("")

        if choice == '1':
            last_name = input("Введіть прізвище: ")
            first_name = input("Введіть ім'я: ")
            salary = float(input("Введіть зарплатню: "))
            conversion = float(input("Введіть конверсію (0-1): "))
            add_personn(last_name, first_name, salary, conversion)

        elif choice == '2':
            get_all_personnel()

        elif choice == '3':
            id = int(input("Введіть ID працівника: "))
            get_personn(id)

        elif choice == '4':
            id = int(input("Введіть ID працівника, якого потрібно видалити: "))
            delet_personn(id)

        elif choice == '5':
            id = int(input("Введіть ID працівника: "))
            calculate_salary_with_bonus(id)

        elif choice == '8':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
    