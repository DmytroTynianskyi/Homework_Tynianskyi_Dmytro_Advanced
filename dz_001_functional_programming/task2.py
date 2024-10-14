# Завдання 2
# Напишіть декоратор, який буде заміряти час виконання для наданої функції.
import time

def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.time()  
        result = func(*args, **kwargs) 
        end = time.time()  
        print(f"{end - start}") 
        return result  
    return wrapper

@stopwatch
def print_hello():
    for i in range(100):
        print("Hello")

print_hello()
