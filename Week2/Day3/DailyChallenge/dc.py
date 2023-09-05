# # Exercise 1 
# usr_word = input ("Enter word: ")
# my_dict = {}
# for idx, char in enumerate(usr_word):
#     if  char not in my_dict:
#         my_dict[char] = []
#     my_dict[char].append(idx)
        
# print(my_dict)

# # Exercise 2
# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = 300
# cart = []

# for item, price in items_purchase.items():
#     int_price = int(price.strip("$").replace(",",""))
#     if int_price <= wallet:
#         # We can add to the cart
#         cart.append(item)
#         # Update the wallet
#         wallet -= int_price
# print(cart)

