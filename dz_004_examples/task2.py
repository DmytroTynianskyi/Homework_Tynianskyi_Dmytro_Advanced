# Завдання 2
# Створіть три функції, одна з яких читає файл на диску
# із заданим ім'ям та перевіряє наявність рядка «Wow!». 
# Якщо файлу немає, то засипає на 5 секунд, а потім знову
# продовжує пошук по файлу. Якщо файл є, то відкриває його
# і шукає рядок «Wow!». За наявності цього рядка закриває 
# файл і генерує подію, а інша функція чекає на цю подію і 
# у разі її виникнення виконує видалення цього файлу. Якщо 
# рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. 
# Створіть файл руками та перевірте виконання програми.
import os
import time
import threading

file_event = threading.Event()

def search_in_file(file_name):
    while not file_event.is_set():
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                if "Wow!" in content:
                    print("Found 'Wow!' in file.")
                    file_event.set() 
                    break
                else:
                    print("No 'Wow!' found, sleeping for 5 seconds.")
        else:
            print(f"File {file_name} not found, sleeping for 5 seconds.")
        time.sleep(5)


def delete_file_on_event(file_name):
    file_event.wait()
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File {file_name} deleted.")


def main(file_name):
    search_thread = threading.Thread(target=search_in_file, args=(file_name,))
    delete_thread = threading.Thread(
        target=delete_file_on_event, args=(file_name,))

    search_thread.start()
    delete_thread.start()

    search_thread.join()
    delete_thread.join()


if __name__ == "__main__":
    file_name = "test_file.txt"
    main(file_name)
