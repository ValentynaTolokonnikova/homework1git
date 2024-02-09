some_people = [
    {
        "name": "John",
        "age": 15,
    },

    {
        "name": "Jack",
        "age": 45,
    },
    {
        "name": "Samanta",
        "age": 15,
    },

    {
        "name": "Peterson",
        "age": 18,
    },

]

min_age = min(person["age"] for person in some_people)
youngest_people = [person["name"] for person in some_people if person["age"] == min_age]

longest_name_len = max(len(person["name"]) for person in some_people)
longest_names = [person["name"] for person in some_people if len(person["name"]) == longest_name_len]

amount_age = sum(person["age"] for person in some_people)
quantity_people = len(some_people)
average_age = amount_age/quantity_people if quantity_people != 0 else 0

print("a) The youngest people:", youngest_people)
print("b) The longest names:", longest_names)
print("c) The average age:", average_age)






# Проверка деления на 0 позволяет предотвратить возможные сбои программы и обеспечить более предсказуемое поведение.
# Вместо того чтобы допустить ошибку деления на 0, можно предпринять соответствующие действия,
# например, вывести сообщение об ошибке,предоставить альтернативное значение или выполнить другую логику обработки.