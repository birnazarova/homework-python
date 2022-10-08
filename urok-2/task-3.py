# Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3} -> 13

n = int(input("Type a number: "))

numbers = []
sum = 0
for i in range(1, n+1):
    x = int(round((1+1/i)**i,0))
    sum += x
    numbers.append(x)
    print(f"{i}: {x}")

print(f"Сумма равна: {sum}")

### Another solution ###

# number = int(input("Введите число N: "))
# list_number = {}
# count = 0
# for i in range(1, number+1):
#     list_number[i] = int(round((1 + 1 / i) ** i, 0))
#     count = count + list_number[i]
# print(list_number, count)