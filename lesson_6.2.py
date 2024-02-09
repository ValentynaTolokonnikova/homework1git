
my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}

keys_set_1 = set(my_dict_1.keys())
keys_set_2 = set(my_dict_2.keys())
print(keys_set_1)
print(keys_set_2)
common_keys = keys_set_1.intersection(keys_set_2)
common_keys_list = list(common_keys)

difference_keys = keys_set_1.difference(keys_set_2)
difference_keys_list = list(difference_keys)

new_dict = {key: my_dict_1[key] for key in difference_keys_list}

merged_dict = {}

for key, value in my_dict_1.items():
    if key in my_dict_2:
        merged_dict[key] = [value, my_dict_2[key]]
    else:
        merged_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        merged_dict[key] = value


print("a) List of common keys:", common_keys_list)
print("b) List with different keys:", difference_keys_list)
print("с) New dictionary:", new_dict)
print("d) Merged dict:", merged_dict)