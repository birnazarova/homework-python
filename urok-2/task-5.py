# Реализуйте алгоритм перемешивания списка.
# import random

# given_list = [1, 6, 3, 679, "some_string"]
# random.shuffle(given_list)
# print(given_list)

### Другой способ ###

import random

given_list = [1, 6, 3, 679, "some_string"]
print(f"Given list: {given_list}")
mixed_list = given_list[:]
list_len = len(mixed_list) 
for i in range(list_len): 
    random_index = random.randint(0, list_len - 1) # 3
    temp_var = mixed_list[i] # нулевой элемент списка mixed_list равен временной переменной temp_var
    mixed_list[i] = mixed_list[random_index] # нулевой элемент списка mixed_list переносим на индекс под рандомным номером
    mixed_list[random_index] = temp_var
print(f"Mixed list: {mixed_list}")






# def mix_list(list_original):
#     # Создаем копию, поскольку мы не должны изменять оригинал
#     list = list_original[:]
#     # Цикл от 0 до длины списка -1
#     list_length = len(list)
#     for i in range(list_length):
#         # Получение случайного индекса
#         index_aleatory = random.randint(0, list_length - 1)
#         # Замена
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     # Возвращаем список
#     return list

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)