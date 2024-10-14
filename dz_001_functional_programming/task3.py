# 3aвдання 3

# Напишіть програму яка буде виводити 25 перших чисел Фібоначі,
# використовуючи для цього три наведені в тексті заняття функції — без кешу,
# з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 
# 10 елементів та з кешем з модулю functools з максимальною кількістю 16 елементів.

from functools import lru_cache


def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)


# Виведення перших 25 чисел Фібоначчі
fib_numbers_no_cache = [fibonacci_no_cache(i) for i in range(25)]
print(fib_numbers_no_cache)

# З кешем довільної довжини:
cache = {}

def fibonacci_with_custom_cache(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        cache[n] = n
    else:
        cache[n] = fibonacci_with_custom_cache(
            n - 1) + fibonacci_with_custom_cache(n - 2)
    return cache[n]


# Виведення перших 25 чисел Фібоначчі
fib_numbers_custom_cache = [fibonacci_with_custom_cache(i) for i in range(25)]
print(fib_numbers_custom_cache)

# З кешем із functools на 10 елементів:
@lru_cache(maxsize=10)
def fibonacci_lru_10(n):
    if n <= 1:
        return n
    return fibonacci_lru_10(n - 1) + fibonacci_lru_10(n - 2)


# Виведення перших 25 чисел Фібоначчі
fib_numbers_lru_10 = [fibonacci_lru_10(i) for i in range(25)]
print(fib_numbers_lru_10)

# З кешем із functools на 16 елементів:
@lru_cache(maxsize=16)
def fibonacci_lru_16(n):
    if n <= 1:
        return n
    return fibonacci_lru_16(n - 1) + fibonacci_lru_16(n - 2)


# Виведення перших 25 чисел Фібоначчі
fib_numbers_lru_16 = [fibonacci_lru_16(i) for i in range(25)]
print(fib_numbers_lru_16)
