# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Type a number: '))
y = int(input('Type a number: '))
z = int(input('Type a number: '))

if not(x or y or z) == (not x and not y and not z):
    print('The statement is correct')
else:
    print('The statement is not correct')