# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input('Type x1: ')) #3
y1 = int(input('Type y1: ')) #2

x2 = int(input('Type x2: ')) #-2
y2 = int(input('Type y2: ')) #-4

result = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(result)