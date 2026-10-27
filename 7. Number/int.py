# Числа в Python  (int)

# Примеры целых чисел:

# 1, -1, 10, 30

number = 1
number2 = 2
number3 = 10

print(f"Число: {number}")
print(f"Число: {number2}")
print(f"Число: {number3}")

# Обработка ошибки 

try:
    user_input_number = int(input("Введите число: "))

    print(f"Ваше число: {user_input_number}")

except:
    print("Ошибка! Это не число!")

