# Практика


number_count = int(input("Введите число от 1 до 5: "))

if number_count < 1 or number_count > 5:
    print("Число превышает лимит...")
else:

    for i in range(number_count):
        name = input("Введите имя: ")

        if name.strip():
            print(f"Привет, {name.strip().upper()}")
        else:
            print("Имя не может быть пустым...")


