# Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3} -> 13

n = int(input("Type a number: "))

numbers = []
sum = 0
for i in range(1, n+1):
    x = int((1+1/n)**n)
    sum += x
    numbers.append(x)
    print(f"{i}: {x}")

print(f"Сумма равна: {sum}")

