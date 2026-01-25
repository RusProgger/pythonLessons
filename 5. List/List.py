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

# удаляет первый найденный элемент по значению
cites.remove("Kiev")
print(cites)

# Удаляет 1-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
cites.pop() # удаляем последний элемент Peter, который был добавлен из списка ext
print(cites)




# Создадим список имен
names = ["Юлия", "Aлена", "Лена", "Людмила"]

# Развернем список 
names.reverse()
print(names)

""""

names = names.reverse()  # names станет None

если нужно занести в отдельную переменную тогда: 

reversed_names = names[::-1]

или 

reversed_names = list(reversed(names))

Все эти методы возвращают None

list.sort()
list.reverse()
list.append()
list.remove()

"""


# list.count(x)	Возвращает количество элементов со значением x

print(names.count("Лена"))