my_value_1 = 2

my_value_2 = "4"

my_value_2 = int(my_value_2)

result = my_value_1 * my_value_2

print(result)
# ответ 8 . my_value_2 из строки превращается в целочисленнре число 4 и * на 2.


# Що буде виведено на екран якщо виконати цей код?
my_value_1 = 2

my_value_2 = "4"

my_value_1 = str(my_value_1)

my_value_2 = int(my_value_2)

result = my_value_1 * my_value_2

print(result)

# ответ 2 превращается с в стрингу, а 4 превращается в целочисленное. уножаем "2"*4, получаем 4 раза по "2" - 2222


my_value_1 = 2

my_value_2 = "4"

my_value_1 = str(my_value_1)

result = my_value_1 + my_value_2

print(result)

my_value = 12

my_bool = my_value % 3 != 0

print(my_bool)

# ответ : False. 12 делим на 3 равно 4.0, остаток от 4.0 - 0. 0 не равно 0 - False.Потому что 0 равен 0.


www = "www.google.com"

if "com" in www:

    print("com in www")

else:

    print("com not in www")

    # ответ. com in www.  т.к. "com" ЕСТЬ в www, то останавливается на первом условии И дальше не идет.




www = "www.command_and_conquer.net"

if "com" in www:

    print("com in www")

else:

    print("com not in www")
# ответ. com in www.  т.к. "com" ЕСТЬ в www, то останавливается на первом условии И дальше не идет.



www = "www.conquer_and_command.net"

if "com" in www:

    print("com in www")

else:

    print("com not in www")
# ответ. com in www.  т.к. "com" ЕСТЬ в www, то останавливается на первом условии И дальше не идет.



www = "www.conquer_and_command.net"

if ".com" in www:

    print("com in www")

else:

    print("com not in www")

# ответ. com not in www.  т.к. ".com" НЕТ в www, то выполняется второе условие



