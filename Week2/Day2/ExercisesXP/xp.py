# Exercise 1
# my_fav_numbers = {2,4,6,8}
# my_fav_numbers.add(10)
# my_fav_numbers.add(12)
# my_fav_numbers.remove(12) # There is no way to remove last number. a set is unordered
# print(my_fav_numbers)

# friend_fav_numbers = {1,3,5}
# our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
# print(our_fav_numbers)

# Exercise 2
# Given a tuple which value is integers, is it possible to add more integers to the tuple? No. It is immutable

# Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# apple_count = basket.count("Apples")
# print(f"There are {apple_count} apples.")
# basket.clear()
# print(basket)


# # Exercise 4
# # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# my_list=[]
# for x in range(3,11, 1):
#     my_list.append(x/2)
# print(my_list)

# # Exercise 5
# for num in range(1, 21):
#     print(num)

# num_list = list(range(1,21))  
# for x in range(len(num_list)):
#     if x % 2 == 0:
#         print(num_list[x])

# Exercise 6
# my_name = 'Sarit'
# usr_name = None
# while usr_name != my_name:
#     usr_name = input("What is your name?")

# Exercise 7
# usr_input = input("Input your favorite fruit(s) (one or several fruits). Separate the fruits with single space")
# fruit_list = usr_input.split(" ")
# usr_fruit = input("Input a name of any fruit")
# if usr_fruit in fruit_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy.")

# Exercise 8
# toppings = []
# usr_input = None
# while True:
#     usr_input = input("Enter topping. Type 'quit' to finish")
#     if usr_input == 'quit':
#         break
#     else:
#         toppings.append(usr_input)
#         print(f"I will add {usr_input} to your pizza.")
# print(toppings)
# print(f"Your total is: {10 + 2.5*len(toppings)}")

# Exercise 9
# Instructions
# usr_input = input("What is the age of each person in the family. Use comma-separated list. ")
# age_list = usr_input.split(",")
# total_cost = 0 
# for age_str in age_list:
#     age = int(age_str)
#     if age < 3:
#         total_cost += 0
#     elif 3 < age < 12:
#         total_cost += 10
#     elif age > 12:
#         total_cost += 15
# print(f"Your total cost is: ${total_cost}")

# name_list = ["Anne", "Bob", "Carrie", "Dave"]
# final_list = []
# for teen in name_list:
#     usr_input = input(f"How old are you {teen}?")
#     age = int(usr_input)
#     if 16 < age < 21:
#         print("You are permitted")
#         final_list.append(teen)
#     else:
#         print("You are not allowed.")
# print(f"{final_list} are permitted")

# Exercise 10
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")

# finished_sandwiches = []
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)

# for sandwich in finished_sandwiches:
#     print(f"I made your {sandwich}")

