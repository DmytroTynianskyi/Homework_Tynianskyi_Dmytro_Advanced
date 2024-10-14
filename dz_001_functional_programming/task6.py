# Завдання 6

# Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в послідовності лише парні числа.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def even_decorator(func):
    def wrapper():
        for num in func():
            if num % 2 == 0:
                yield num
    return wrapper


@even_decorator
def even_fibonacci():
    return fibonacci_generator()

for i, num in enumerate(even_fibonacci()):
    if i == 100:
        break
    print(num)
