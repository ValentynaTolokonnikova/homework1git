# # Task_1

#
# print("Calculator")
#
# first_number = float(input("type first number:"))
# operation = input("Select operation:+,-,*,/")
# second_number = float(input("type second number:"))
#
# result = 0
#
# if operation == "+":
#     result = first_number+second_number
# elif operation == "-":
#     result = first_number-second_number
# elif operation == "*":
#     result = first_number*second_number
# elif operation == "/" and second_number == 0:
#     result = "Zero Division Error"
# elif operation == "/":
#     result = first_number / second_number
#
# print(result)                                     # одна точка входа и одна точка выхода, поэтому один принт, после всех




#
#
# # Task_2
#
# value_list_1 = [12, 3, 4, 10]
# new_list_1 = value_list_1[-1:] + value_list_1[0:3] # Так як ти не знаєш скільки елементів всього,
# print(new_list_1)                                  # доводиться перестворювати і переписувати умову
#                                                    # (ручками вписувати, то 3 то 4)

value_list_1 = [12, 3, 4, 10]
new_list_1 = value_list_1[-1:] + value_list_1[0:-1]
print(new_list_1)
#
# value_list_2 = [1]
# print(value_list_2[0:1])   # здесь вызывается список, как требуется в задании - [1]
# print(value_list_2[0])   # здесь вызывается элемент списка, поэтому - 0 (номер индекса элемента)
# #
# value_list_3 = []
# print(value_list_3)
#
# value_list_4 = [12, 3, 4, 10, 8]
# new_list_4 = value_list_4[-1:] + value_list_4[0:4]
# print(new_list_4)

# #*******************
#
# value_list_1 = [12, 3, 4, 10]
# new_list_1 = value_list_1[-1:] + value_list_1[0:-1]
# print(new_list_1)
#
# value_list_4 = [12, 3, 4, 10, 8]
# new_list_4 = value_list_4[-1:] + value_list_4[0:-1]
# print(new_list_4)
#
#


# first_symbol = float(input("1st num:  "))
# operator = input("operator:  ")
# second_symbol = float(input("2nd num:  "))
#
# # result = 0
#
# # if operator not in "+-*/" or len(operator) != 1:
# if operator not in ["+", "-", "*", "/"]:
#     result = "ERROR - something goes wrong"
# elif operator == "+":
#     result = first_symbol + second_symbol
# elif operator == "-":
#     result = first_symbol - second_symbol
# elif operator == "*":
#     result = first_symbol * second_symbol
# elif operator == "/" and second_symbol == 0:
#     result = "ERROR - can't divide by zero"
# elif operator == "/":
#     result = first_symbol / second_symbol
# else:
#     result = "hhhhhh"
#
# print(result)












