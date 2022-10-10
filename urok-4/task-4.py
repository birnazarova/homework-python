# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = input("Задайте степень: ")
result = str(random.randint(0,101))+'x**' + k + ' + ' + str(random.randint(0,101))+'x + '+str(random.randint(0,101)) + ' = 0'

with open ('/Users/aika/Desktop/Git/python/homework-python/urok-4/file4.txt', 'w') as file:
    file.write(result)