# В цикле получите от пользователя названия четырёх цветов и сохраните их в список. Выведите получившийся список на экран.

color = []

for i in range(4):
    color_input = input(f"Введите цвет {i + 1}: ")
    color.append(color_input)

print("---------------------------")
print(color)

print("---------------------------")
print(color[0])
print(color[1])
print(color[2])
print(color[3])