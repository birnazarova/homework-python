# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# i = int(input("Type a number: "))

# binary = []
# i=2
# if i%2!=0:  
#     binary.append(1)

# while i > 1:
#     i = i//2
#     if i%2==0:
#         binary.append(0)
#     else:
#         binary.append(1)
# print(binary)

### Another solution ###

a = int(input('введите число для перевода = '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a = a // 2
print(b)
