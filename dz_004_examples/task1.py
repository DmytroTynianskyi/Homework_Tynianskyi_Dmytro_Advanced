# Завдання 1
# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань,
# використовуючи Thread, і заміряйте швидкість їхнього виконання, а потім
# заміряйте швидкість обчислення, використовуючи той же набір завдань на
# ThreadPoolExecutor. Як приклади використовуйте останні значення, від
# мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_factorial(n):
    print(f"Factorial of {n}: {factorial(n)}")


def execute_with_threads(numbers):
    threads = []
    for n in numbers:
        thread = threading.Thread(target=calculate_factorial, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def execute_with_thread_pool(numbers):
    with ThreadPoolExecutor() as executor:
        executor.map(calculate_factorial, numbers)


if __name__ == "__main__":
    numbers = [5, 10, 20, 50, 100, 150, 200, 250] 

    start_time = time.time()
    execute_with_threads(numbers)
    print(f"Execution with threads took {time.time() - start_time:.5f} seconds\n")

    start_time = time.time()
    execute_with_thread_pool(numbers)
    print(f"Execution with ThreadPoolExecutor took {time.time() - start_time:.5f} seconds\n")





































