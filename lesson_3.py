# Task_1


print("Calculator")

first_number = int(input("type first number"))
second_number = int(input("type second number"))
operation = input("Select operation:+,-,*,/")

if operation == "+":
    print(first_number+second_number),
elif operation == "-":
    print(first_number-second_number),
elif operation == "*":
    print(first_number*second_number),
elif operation == "/":
    if second_number != 0:
        print(first_number/second_number)
    else:
        print("ZeroDivisionError")


# Task_2

value_list_1 = [12, 3, 4, 10]
new_list_1 = value_list_1[-1:] + value_list_1[0:3]
print(new_list_1)

value_list_2 = [1]
print(value_list_2[0:1])   # здесь вызывается список, как требуется в задании - [1]
#print(value_list_2[0])   # здесь вызывается элемент списка, поэтому - 1

value_list_3 = []
print(value_list_3)

value_list_4 = [12, 3, 4, 10, 8]
new_list_4 = value_list_4[-1:] + value_list_4[0:4]
print(new_list_4)

















#
# first_number = int(input("type first number"))
# print(first_number)
# input("type '+' sign")
# second_number = int(input("type second number"))
# sum = first_number+second_number
# input("type '=' sign")
# print(f"Sum is {sum}")
#
#
# first_number = int(input("type first number"))
# print(first_number)
# input("type '-' sign")
# second_number = int(input("type second number"))
# print(second_number)
# diff = first_number-second_number
# input("type '=' sign")
#
# print(f" Difference is {diff}")
#
# first_number = int(input("type first number"))
# print(first_number)
# input("type '*' sign")
# second_number = int(input("type second number"))
# print(second_number)
# mult = first_number*second_number
# input("type '=' sign")
#
# print(f" Product is {mult}")
#
# first_number = int(input("type first number"))
# print(first_number)
# input("type '/' sign")
#
# second_number = int(input("type second number"))
# div = first_number/second_number
# if second_number != 0:
#     print(first_number/second_number)
# else:
#     print("ZeroDivisionError")



