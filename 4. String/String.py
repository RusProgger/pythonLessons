# Работа со строками 

s = "Hello"
y = "World"
print(f"{s}{y}")

# '''''' - создание больших строк

text = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing 
Lorem Ipsum passages, and more recently with desktop publishing software like 
Aldus PageMaker including versions of Lorem Ipsum.
'''

print(text)

# Получение длины строки:

print(f"Длина строки: {len(text)}")

# Конкатенация (объединение) строк:

wel = "Hello " + "World!!!"

print(wel)


# Повторение строки n раз:

test = "My"

print(f"{test * 3}")


# Индексация и срезы:

name = "I love Python"

print(name[0])    
print(name[-1])   
print(name[1:4])

# Проверка содержимого строки состоит ли строка из цифр: 

name1 = "avc"
print(name1.isdigit())
name_int = "234"
print(name_int.isdigit())

# isalpha() — проверяет только буквы
# isdigit() — проверяет только цифры

print(name_int.isalpha())
print(name1.isalpha())

# Методы строк:

abzac = "hello, my name is alex"
print(abzac.upper())
print(abzac.capitalize())






