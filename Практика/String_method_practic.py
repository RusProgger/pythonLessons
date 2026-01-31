# Практика


number_count = int("Введите число от 1 до 5: ")

if number_count > 6:
    print("Число превышает лимит...")
else:

    for i in range(number_count):
        name = input("Введите имя: ")


if name != "":
    print(f"Привет, {name.strip().upper()}")
else:
    print("Имя не может быть пустым...")