




















print(1 + 2 + 3)
value = 1 * 2 * 3

print(value)
value = "1 * 2 * 3"

print(value)
value = "1" + "2" + "3"

print(value)
value = "1" + "2" * 3

print(value) # ответ 1222. двойка повторилась 3 раза и склеилась с 1. Почему ? Порядок действий?
# сначала * или /, а потом + или - ? Т.е. мы сначала 3 раза повторяем двойку, и просто приклеиваем ее к единице?

value = ("1" + "2") * 3

print(value) # ответ 121212. склеили значение строки, сначала в скобках, и повторили его 3 раза.

value_1 = 2

value_2 = 4

result = value_1 * value_2

print(result)

value_1 = 2

value_2 = "4"

result = value_1 * value_2

print(result) # ответ 44. дважды повторяем строку со значением 4.

value_1 = "2"

value_2 = 4

result = value_1 * value_2

print(result) # ответ 2222. четыре раза повторяем строку со значением 2 .

value_1 = "2"

value_2 = "4"

result = value_1 + value_2

print(result) # ответ 24. просто склеили значение строк 2 и 4.