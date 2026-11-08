# Калькулятор скидок

const = float(input("Введите стоимость товара: "))

if const <= 0:
    print("Ошибка! Цена товара должна быть больше нуля.")

elif const < 100:
    discount_percent = 0

elif const < 500:
    discount_percent = 5

elif const < 1000:
    discount_percent = 10

else:
    discount_percent = 20

if const > 0:
    discount = const * discount_percent / 100
    result = const - discount

    print(f"Первоначальная цена: {const}")
    print(f"Скидка: {discount_percent}%")
    print(f"Сумма скидки: {discount}")
    print(f"Итого: {result}")
