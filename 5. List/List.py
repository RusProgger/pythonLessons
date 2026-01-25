# Списки

cites = ["Kiev", "Odessa", "Ujgorod", "Poltava"]

# Проверяем какой из типов данных хранит переменная 
print(type(cites))

# Добавим елемент в конец списка
cites.append("Черкассы")

# Вывод списка
print(cites)

# Расширяет список list, добавляя в конец все элементы списка 
ext = ["Moskow", "Peter"]

cites.extend(ext)

print(cites)

# Вставляет на i-ый элемент значение x
cites.insert(-1, ("MMM", "DDD"))

print(f"Елемент: {cites}")