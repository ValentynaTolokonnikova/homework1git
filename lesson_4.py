# # Task 4.1

value_list_1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for num in value_list_1:
    if num == 0:
        value_list_1.remove(0)
        value_list_1.append(0)
print(value_list_1)


# # Task 4.2

list_1 = []                               #исправлен, добавлена проверка на пустой список
if not list_1:
    list_1 = 0
    print(list_1)
else:
    list_1 = sum(list_1[::2]) * list_1[-1]
    print(list_1)






#
# list_1 = [0, 1, 7, 2, 4, 8]
# list_2 = (list_1[::2])
# new_list = sum(list_2) * list_1[-1]
# print(new_list)


