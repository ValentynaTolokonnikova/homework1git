# Task 4.1

value_list_1 = [0, 1, 0, 12, 3]
for num in value_list_1:
    if num == 0:
        value_list_1.remove(0)
        value_list_1.append(0)
print(value_list_1)




# Task 4.2


list_1 = [0, 1, 7, 2, 4, 8]
new_list = sum(list_1[::2]) * list_1[-1]
print(new_list)








#
# list_1 = [0, 1, 7, 2, 4, 8]
# list_2 = (list_1[::2])
# new_list = sum(list_2) * list_1[-1]
# print(new_list)


