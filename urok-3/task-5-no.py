# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
    
# def fibonacci(n):
#     if n in [-1,1,2]:
#         return 1
#     elif n == -2:
#         return -1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# list = []
# list_negative = []
# user_n = 8
# for i in range(0, user_n + 1):
#     list_negative.insert(0, fibonacci(i) * ((-1)**(i+1)))
# for i in range(1, user_n + 1):
#     list_negative.append(fibonacci(i))
# for i in list_negative:
#     print(i, end = " ")

### Another solution with recursion ###

def nega_fibonacci(numb):
    array = [1,0,1]
    for i in range(1, numb):
        array.insert(0, array[1] - array[0])
        array.append(array[-2] + array[-1])
    return array

num = int(input("Input some number: "))
print(nega_fibonacci(num))