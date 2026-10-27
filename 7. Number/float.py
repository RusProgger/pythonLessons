# Числа Float

f_number = 10.5

print(f_number)

f_num1 = 10.2

f_num2 = 2.2

print(f_num1 / f_num2)

# Округление используем round

print(round(f_num1 / f_num2, 2))

# Второй способ 

print(f"Второй способ округления: {f_num1 / f_num2:.2f}")


# Попросим пользователя ввести данные вес, а также вывод значения после запятой



# Обработка ошибки если пользователь введет некорректное число

try:
    weight = float(input("Введите вес: "))
    print(f"Ваш вес: {round(weight, 2)}")

except:
    print("Ошибка ввода!")