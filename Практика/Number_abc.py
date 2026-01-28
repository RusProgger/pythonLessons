# Дано трехзначное число. Найдите сумму его цифр.

number = int(input())
number_a = number // 100 # Находим сотки
number_b = (number // 10) % 10 # Находим 10
number_c = number % 10 # единицы

print()  