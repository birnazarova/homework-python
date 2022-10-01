# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Type a number from 1 to 7: '))

if day in range (1,8):
    if day == 6 or day == 7:
        print('yes')
    else:
        print('no')
else: 
    print('You provided an incorrect number')
