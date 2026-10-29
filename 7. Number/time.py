time = int(input("Введите кол-во секунд: "))

try:
    # minute
    minute = time // 60

    # second

    second = time % 60

    print(f"{time} = {minute} минут и {second} секунд")

except:
    print("Ошибка ввода! Это не число!")

