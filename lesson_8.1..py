def add_one(some_list):
    num_str = int("".join(map(str, some_list)))
    num_str += 1
    num_list = list(map(int, str(num_str)))
    return num_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")










# some_list = [1, 2, 3, 4]
# num_str = int("".join(map(str, some_list)))
# num_str += 1
# num_list = list(map(int, str(num_str)))
# print(num_list)
