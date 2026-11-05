a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7}

print(a & b)

print("\n--------------------------\n")

num = [20, 30, 50, 100]

num2 = [10, 50, 70, 120]

print(num + num2) # [20, 30, 50, 100, 10, 50, 70, 120]

print("\n------------ Сладывание --------------\n")

result = [num1 + num2 for num1, num2 in zip(num, num2)]

print(f"Результат: {result}")