# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

some_list = [2, 3, 5, 6]
result = []
if len(some_list)%2!=0:
    for i in range(len(some_list)//2+1):
        result.append(some_list[i]*some_list[(-1-i)])
else:
    for i in range(len(some_list)//2):
        result.append(some_list[i]*some_list[(-1-i)])
print(result)