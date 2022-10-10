# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Type a number: "))

mnojiteli = []
divider = 2

while N > 1:
    while N % divider == 0:
        mnojiteli.append(divider)
        N //= divider
    divider += 1
print(mnojiteli)

