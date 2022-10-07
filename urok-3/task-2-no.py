# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

some_list = [2, 3, 4, 5, 6]
reversed_list = [6, 5, 4, 3, 2]

result = []
multiplied = 0

for i in range(0, len(some_list)//2):
    for j in range(len(some_list), 0):
        multiplied = some_list[i]*some_list[j]
        print(f"{some_list[i]}*{some_list[j]}")

# for i in range(0, len(some_list)//2):
#     for j in range(0, len(reversed_list)//2):
#         multiplied = some_list[i]*reversed_list[j]

# for i in some_list:
#     for j in reversed_list:
#         multiplied = i*j
#         print(multiplied)