# В цикле получите от пользователя названия четырёх цветов и сохраните их в список. Выведите получившийся список на экран.

color = []

for i in range(4):
    color_input = input(f"Введите цвет {i + 1}: ")
    color.append(color_input)
print(color)
