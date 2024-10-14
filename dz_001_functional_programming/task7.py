# Завдання 7
# Створіть звичайну функцію множення двох чисел. Створіть карированну функцію 
# множення двох чисел. Частково застосуйте її до одного аргументу, до двох аргументiв.

def multiply(x, y):
    return x * y

def curry_multiply(x):
    def multiply_by_x(y):
        return x * y
    return multiply_by_x

multiply_by_2 = curry_multiply(2)
print(multiply_by_2(5))  
print(multiply_by_2(3))  
