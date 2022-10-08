# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = list(map(int, input("type a sequence of numbers: ").split()))
print(n)
n2 = []
for i in n:
    if n.count(i) <= 1:
        n2.append(i)
print(n2)