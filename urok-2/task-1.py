# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# N = input("Type a number: ")

# digits = []
# for i in range(len(N)):
#     digits.append(int(N[i]))

# sum = 0
# for i in range(len(digits)):
#     sum = sum + digits[i]
# print(sum)

### Teacher's solution ###

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

### Another solution ###

data1 = "0.456"
for i in data1:
    print(i)
print(sum([int(i) for i in data1 if i.isdigit()]))