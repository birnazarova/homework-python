# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

some_list = [1.1, 1.2, 3.1, 5, 10.01]

max_particle = 0
min_particle = 1

for i in some_list:
    if round(i-int(i),2) > max_particle:
        max_particle = round(i-int(i),2)
print(max_particle)

for i in some_list:
    if 0 < round(i-int(i),2) < min_particle:
        min_particle = round(i-int(i),2)
print(min_particle)

print(f"Результат равен {max_particle-min_particle}")