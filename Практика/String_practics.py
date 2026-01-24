# Строки практика

s = "Python is awesome"

print(len(s)) # Длина строки
print(s[0]) # Первый символ
print(s[-1]) #  Последний символ
print(s[7:-8]) # Выводим is с помощью среза

# Задание 2 — работа со срезами

word = "Programming"

print(word[:5])
print(word[-3:])
print(word[1:-1])
print(word[::-1])


# Задание 3 — проверки строки

a = "12345"
b = "abc123"
c = "Hello"

print(f"Строка {a}, состоит из цифр: {a.isdigit()}")
print(f"Строка {b}, состоит из букв: {b.isalpha()}")
print(f"Строка {c}, состоит из букв: {c.isalpha()}")