# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

k = 8
fibonacci = []
n = 1

# for i in fibonacci:
#     fibonacci.append(0)
#     fibonacci.append(1)
#     # fibonacci.append(fibonacci[i]+fibonacci[i-1])
# print(fibonacci)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
i = 0
while i < 30:
    number = i+(i-1)
    print(number)