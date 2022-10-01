# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

N = input("Type a number: ")

digits = []
for i in range(len(N)):
    digits.append(int(N[i]))

sum = 0
for i in range(len(digits)):
    sum = sum + digits[i]
print(sum)
