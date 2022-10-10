# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('/Users/aika/Desktop/Git/python/homework-python/urok-4/file1.txt', 'r') as file:
    string1 = file.read()

with open('/Users/aika/Desktop/Git/python/homework-python/urok-4/file2.txt', 'r') as file:
    string2 = file.read()

result = 0
result = string1 + ' + ' + string2
print(result)

with open ('/Users/aika/Desktop/Git/python/homework-python/urok-4/file3.txt', 'w') as file:
    file.write(result)