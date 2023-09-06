from random import shuffle


user_str = input("Input string that is 10 characters long")
if len(user_str) < 10:
    print("string not long enough.")
elif len(user_str) > 10:
    print("string too long.")
else: 
    print("perfect string")
    print(f"First letter {user_str[0]} and last letter {user_str[-1]}")
    # for x in range(len(user_str) + 1):
    #     print(user_str[0:x])
    new_string = ""
    for letter in user_str:
        new_string += letter
        print(new_string)
    
    string_list = list(user_str)
    shuffle(string_list)

    shuffled_string = ''.join(string_list)

    print("Shuffle Bonus " + shuffled_string)