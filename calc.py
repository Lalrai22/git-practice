# Простой калькулятор на функциях

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    # проверяем деление на ноль
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


print(add(5, 3))
print(sub(10, 4))
print(mul(2, 6))
print(div(8, 2))
