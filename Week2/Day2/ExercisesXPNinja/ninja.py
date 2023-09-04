import math 
import random

# # Exercise 1
# usr_input = input("Please enter a comma-separated string of numbers")
# num_list = [int(x) for x in usr_input.split(',')]
# c = 50
# h = 30
# results = []
# for d in num_list:
#     q = round(math.sqrt((2*c*d)/h))
#     results.append(q)
# print(results)

# # Exercise 2
# my_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]  # Store the list of numbers in a variable
# my_sum = sum(my_list)
# print(my_list) # The list of numbers – printed in a single line
# print(sorted(my_list, reverse=True)) # The list of numbers – sorted in descending order (largest to smallest) 
# print(my_sum) # The sum of all the numbers
# print([my_list[0], my_list[-1]]) # A list containing the first and the last numbers.
# print([x for x in my_list if x>50]) # A list of all the numbers greater than 50.
# print([x for x in my_list if x<10]) # A list of all the numbers smaller than 10.
# print([x**2 for x in my_list]) # A list of all the numbers squared 
# my_set = set(my_list)
# print(f"My set {my_set} contains {len(my_set)} numbers")#The numbers without any duplicates – also print how many numbers are in the new list.
# print(my_sum/len(my_list)) # The average of all the numbers.
# print(max(my_list)) # The largest number.
# print(min(my_list)) # The smallest number.

# # Bonus: Find the sum, average, largest and smallest number without using built in functions.
# hard_sum = 0
# hard_max = my_list[0]
# hard_min = my_list[0]
# for x in my_list:
#     hard_sum += x
#     if x > hard_max:
#         hard_max = x
#     if x < hard_min:
#         hard_min = x
# hard_average = hard_sum/len(my_list)
# print(f"sum: {hard_sum}, average: {hard_average}, largest: {hard_max}, smallest: {hard_min}")

# # Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
# user_numbers = []
# for x in range(10):
#     usr_input = input("Number from -100 to 100 (comma-separated).")
#     usr_num = int(usr_input)
#     user_numbers.append(usr_num)
# print(user_numbers)

# # Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# random_list = random.sample(range(-100, 101), 10)
# print(random_list)

# # Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# random_size = random.randint(50)
# print(random_size)
# #Bonus: Will the code work when the number of random numbers is not equal to 10?
# ## Yes

# # Exercise 3 
# my_paragraph = "In my younger and more vulnerable years, my father gave me some advice that I've been turning over in my mind ever since. 'Whenever you feel like criticizing any one,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.'"
# print(my_paragraph)
# print(f"This paragraph has {len(my_paragraph)} characters")
# sentence_count = my_paragraph.count('.')
# print(f"This paragraph contains {sentence_count} sentences")
# words = my_paragraph.split(' ')
# word_count = len(words)
# print(f"This paragraph contains {word_count} words")
# print(f"This paragraph contains {len(set(words))} unique words")

# no_spaces = "".join(my_paragraph.split())
# print(f"This paragraph has {len(no_spaces)} non-whitespace characters")
# print(f"This paragraph has an average of {word_count/sentence_count} words per sentence")
# print(f"There are {word_count - len(set(words))} non-unique words")

# # Exercise 4
# sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
# word_freq = {}
# for word in sentence.split(' '):
#     if word not in word_freq:
#         word_freq[word] = 0 
#     word_freq[word] += 1
# print(word_freq)