# # Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# my_dict = dict(zip(keys, values))
# print(my_dict)

# # Exercise 2

# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8} #

# #  Bonus:
# family = {}
# while True:
#     name = input("Enter a family member's name (or press Enter to finish): ")
#     if not name:
#         break
#     age = int(input(f"Enter {name}'s age: "))
#     family[name] = age

# price = 0
# for person in family:
#     age = family[person]
#     if age < 3:
#         price += 0 
#     elif 3 <= age <  12:
#         price += 10
#     elif age > 12:
#         price += 15
# print(f"The total cost for the family is ${price}")

# # Exercise 3
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]
#     }


# }

# brand["number_stores"] = 2 # Change the number of stores to 2.
# print(brand) 

# print(f"Zara clients are people for are shopping for {', '.join(brand['type_of_clothes'])} fashion") # Print a sentence that explains who Zaras clients are.


# brand["country_creation"] = "Spain" # Add a key called country_creation with a value of Spain.
# print(brand) 

# if "international_competitors" in brand: 
#      #Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
#     brand["international_competitors"].append("Desigual") 
# print(brand)

# brand.pop("creation_date") # Delete the information about the date of creation.
# print(brand)

# print(brand["international_competitors"][-1]) # Print the last international competitor.

# print(brand["major_color"]["US"])# Print the major clothes colors in the US. 

# print(len(brand))# Print the amount of key value pairs (ie. length of the dictionary).

# print(brand.keys())# Print the keys of the dictionary.

# # Create another dictionary called more_on_zara with the following details:
# # creation_date: 1975 
# # number_stores: 10 000
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
# brand.update(more_on_zara) # Use a method to add the information from the dictionary more_on_zara to the dictionary brand. 

# print(brand["number_stores"])# Print the value of the key number_stores. 

# # Exercise 4
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# #1/
# disney_users_A = {user: index for index, user in enumerate(users)}
# print(disney_users_A)
# #2/
# disney_users_B = {index: user for index, user in enumerate(users)}
# print(disney_users_B)
# #3/ 
# disney_users_C = dict(sorted(disney_users_A.items()))
# print(disney_users_C)

# disney_users_D = {user: index for index, user in enumerate(users) if "i" in user}
# print(disney_users_D)

# disney_users_E = {user: index for index, user in enumerate(users) if user.startswith(("M","P"))}
# print(disney_users_E)
