# Форматы выводов 
name = input("Как вас зовут: ")
# Вывод через запятую, (старый способ)
print("Привет", name)

# % - форматирование (старый, но живой)

print("Этот вывод через - форматирование \nПривет %s" % (name))

# f-строки актуальный 

print(f"Вывод через f-строки: \nПривет, {name}")

# print c параметрами sep и end

print("a", "b", "c", sep=" | ", end="!\n")

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets.\n It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged.\n It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.""", end="!!!\n")
