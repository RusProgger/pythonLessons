# Практика

# Задача чётное или нечетное число

number = int(input("Введите число: "))
if number % 2 == 0 and number > 0:
    print(f"Число {number} положительное и чётное")
else:
    print(f"Число {number} не подходит..")

# Дополенение к задаче 

number = int(input("Введите число: "))
if number % 2 == 0 and number > 0:
    print(f"Число {number} положительное и чётное")
elif number < 0:
    print(f"Число {number} Отрицательное")
elif number == 0:
    print(f"Число {number} Ноль")
else:
    print(f"Число {number} положительное но не чётное..")
