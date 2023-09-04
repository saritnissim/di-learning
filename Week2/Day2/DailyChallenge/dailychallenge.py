# # Exercise 1
# usr_num_str = input("Input number")
# usr_len_str = input("Input length")
# usr_num = int(usr_num_str)
# usr_len = int(usr_len_str)

# result = [usr_num]
# for x in range(1,usr_len) :
#     result.append(result[x-1]+usr_num)
# print(result)

# # Exercise 2
# usr_str = input("Input string")
# result = usr_str[0]
# pointer = 0
# for char in usr_str:
#     #If the result string does not have the letter, add it
#     if result[pointer] != char:
#         result += char
#         pointer += 1
# print(result)