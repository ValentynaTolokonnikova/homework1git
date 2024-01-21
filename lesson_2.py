input_number = input("Type 4 integer numbers")
input_number = int(input_number)
result_1 = (input_number // 1000)
result_2 = (input_number // 100 % 10)
result_3 = (input_number // 10 % 10)
result_4 = (input_number % 10)


print(result_1)
print(result_2)
print(result_3)
print(result_4)

