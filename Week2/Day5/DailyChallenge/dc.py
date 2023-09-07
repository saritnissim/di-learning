# Challenge 1 : Sorting
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#     Use List Comprehension
# def sort_alpha(*args):
#     output = []
#     for arg in args:
#         pass



# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


# # Challenge 2 : Longest Word
# # Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word. (Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# def longest_word(sentence):
#     longest_len = 0
#     longest_word = ""

#     for word in sentence.split():
#         word_len = len(word)
#         if word_len > longest_len:
#             longest_len = word_len
#             longest_word = word
#     return(longest_word)

# print(longest_word("Margaret's toy is a pretty doll."))


# # Advanced Challenge
# # Here is a python code that generate a list of 20000 random numbers, called list_of_numbers.
# # Extend this code to guess how many couples of numbers in list_of_numbers sum to target_number.
## Note: I wasn't able to finish running the code. Maybe there is a better way
# import random
# couples = []
# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# target_number   = 3728
# list_of_numbers_filtered = [x < target_number + 1 for x in list_of_numbers]
# for idx1 in range(0,len(list_of_numbers_filtered)):
#     for idx2 in range(idx1+1,len(list_of_numbers_filtered)):
#         num1 = list_of_numbers_filtered[idx1]
#         num2 = list_of_numbers_filtered[idx2]
#         if num1 + num2 == target_number:
#             couples.append((num1,num2))
# print(couples)
