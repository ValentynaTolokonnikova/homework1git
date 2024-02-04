# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True


my_string = input("Please enter smth:")
result = False

if my_string.isidentifier():
    if my_string == "_" or my_string.islower():
        result = True

print(result)