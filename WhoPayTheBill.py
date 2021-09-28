import random

name = input("Enter names seperated by a comma : ")
name_list = name.split(", ")
number_item = len(name_list)

random_choice = random.randint(0,(number_item-1))
print(name_list[random_choice] + " is going to pay today's meal.💸😋")