#Easy
#Задание - 1 
First_list = [2, 4, 6, 8, 0]
Second_list = [i ** 2 for i in First_list]

#Задание - 2
First_fruits = ["виноград", "апельсин", "вишня", "черешня", "слива", "абрикос"]
Second_fruits = ["арбуз", "дыня", "абрикос", "инжир", "виноград", "мушмула"]
Repetitive_fruits = [i for i in First_fruits and Second_fruits if i in First_fruits and i in Second_fruits]
print(Repetitive_fruits)

#Задание - 3
list_1 = [12, 45, 23, 48, 6, 88, 32, 95, -27, -92, 36, 0]
list_2 = [i for i in list_1 if i %3 == 0 and i %4 == 0 and i > 0]
print(list_2)
