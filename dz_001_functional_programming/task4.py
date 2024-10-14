# Завдання 4

# За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих 4х варіантів.
import time
from functools import lru_cache


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start}")
        return result
    return wrapper


def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)



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



fib_numbers_custom_cache = [fibonacci_with_custom_cache(i) for i in range(25)]
print(fib_numbers_custom_cache)

# З кешем із functools на 10 елементів:


@lru_cache(maxsize=10)
def fibonacci_lru_10(n):
    if n <= 1:
        return n
    return fibonacci_lru_10(n - 1) + fibonacci_lru_10(n - 2)




fib_numbers_lru_10 = [fibonacci_lru_10(i) for i in range(25)]
print(fib_numbers_lru_10)

# З кешем із functools на 16 елементів:


@lru_cache(maxsize=16)
def fibonacci_lru_16(n):
    if n <= 1:
        return n
    return fibonacci_lru_16(n - 1) + fibonacci_lru_16(n - 2)



fib_numbers_lru_16 = [fibonacci_lru_16(i) for i in range(25)]
print(fib_numbers_lru_16)


@time_decorator
def fibonacci_no_cache_decorated(n):
    return fibonacci_no_cache(n)


@time_decorator
def fibonacci_with_custom_cache_decorated(n):
    return fibonacci_with_custom_cache(n)


@time_decorator
def fibonacci_lru_10_decorated(n):
    return fibonacci_lru_10(n)


@time_decorator
def fibonacci_lru_16_decorated(n):
    return fibonacci_lru_16(n)
