# Факториал числа

def Fact(f):
    f_result = 1

    for i in range(1, f + 1):
         f_result *= i
         
    return f_result


number = int(input("Введите число: "))
result = Fact(number)

print(f"Факториал числа: {result}")

    