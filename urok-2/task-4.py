# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# N = int(input("Type a number: "))
# N_list = []
# for i in range(-N, N+1):
#     N_list.append(int(i))
# print(N_list)

n = int(input("Задайте число: "))
position_1 = int(input('Позиция 1: '))
position_2 = int(input('Позиция 2: '))
list_numbers = []
for i in range(-n, n+1):
    list_numbers.append(i)
    print(f"{i},", end =" ")
print(list_numbers, list_numbers[position_1 - 1] * list_numbers[position_2 - 1])