import random
# # Exercise 1 
# list_a = [2,4,6,8]
# list_b = [1,3,5,7]
# concat_list = list_a + list_b
# print(concat_list)

# # Exercise 2
# multiples_of_5_and_7 = []
# for x in range(1500,2500 + 1):
#     if x % 5 ==0 or x % 7 == 0:
#         multiples_of_5_and_7.append(x)
# print(multiples_of_5_and_7)

# # Exercise 3
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# usr_input = input("What is your name. ")

# if usr_input in names:
#     indexOfName = names.index(usr_input)
#     print(f"Index of {usr_input} is {indexOfName}")

# # Exercise 4
# num_list = []
# num_1 = int(input("Input the 1st number: "))
# num_2 = int(input("Input the 2nd number: "))
# num_3 = int(input("Input the 3rd number: "))

# num_list= [num_1, num_2, num_3]
# num_list.sort()
# print(f"The greatest is {num_list[-1]}")


# # Exercise 5
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for letter in alphabet:
#     if letter in "aeiou":
#         print(f"{letter} is a vowel.")
#     else:
#         print(f"{letter} is a consonant.")

# # Exercise 6
# usr_input = input("Give 7 words separated by space ")
# words = usr_input.split(' ')
# letter = input("Give me a character. ")
# for word in words:
#     if letter in word:
#         print(word.index(letter))
#     else:
#         print(f"Sorry, letter {letter} is not in the word {word}")

# # Exercise 7
# million_list = list(range(1,1000001))
# print(f"min: {min(million_list)}, max: {max(million_list)}")
# sum = 0
# for x in million_list:
#     sum += x
# print(f"The sum is {sum}.")

# # Exercise 8
# input_sequence = input("Enter a sequence of comma-separated numbers: ")
# numbers = input_sequence.split(',')
# num_list = list(numbers)
# num_tuple = tuple(numbers)

# print(num_list)
# print(num_tuple)

# # Exercise 9
# wins = 0
# losses = 0

# while True:
#     random_number = random.randint(1, 9)
#     usr_input = input("Input number from 1 to 9. 'q' to quit")
#     if usr_input != "q":
#         usr_num = int(usr_input)

#         if usr_num == random_number:
#             print("Winner!")
#             wins += 1
#         else:
#             print("Better luck next time")
#             losses +=1 
#     else:
#         break;
# print(f"Wins: {wins}, Losses: {losses}")