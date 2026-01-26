# Практика 2 Работа со списками

users_name = []

# Справшиваем ввод пользователя сколько он хочет ввести 

number = int(input("Введите число: "))

for num in range(number):
    inp = input(f"Введите имя {num + 1}: ")
    users_name.append(inp)

print(users_name)
