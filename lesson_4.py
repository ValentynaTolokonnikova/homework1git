# Task 4.1
#
# value_list_1 = [0, 1, 0, 12, 3]
# for num in value_list_1:
#     if num == 0:
#         value_list_1.remove(0)
#         value_list_1.append(0)
# print(value_list_1)
#
#
# value_list_2 = [0]
# for num in value_list_2:
#     if num == 0:
#         value_list_2.remove(0)
#         value_list_2.append(0)
# print(value_list_2)
#
#
# value_list_3 = [1, 0, 13, 0, 0, 0, 5]
# for num in value_list_3:
#     if num == 0:
#         value_list_3.remove(0)
#         value_list_3.append(0)
# print(value_list_3)
#
#
# value_list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# for num in value_list_4:
#     if num == 0:
#         value_list_4.remove(0)
#         value_list_4.append(0)
# print(value_list_4)


# Task 4.2
#[0, 1, 7, 2, 4, 8] -> (0 + 7 + 4) * 8 = 88

# list_1 = [0, 1, 7, 2, 4, 8]
# result = (list_1[::2])
# result = sum(result) * list_1[-1]
# print(result)

list_1 = [0, 1, 7, 2, 4, 8]
new_list = sum(list_1[::2]) * list_1[-1]
print(new_list)


