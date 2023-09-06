# Timed Challenge
# def char_count(str, char):
#     return str.count(char)

# print(char_count("This is me", "i"))

# # Exercise 1 : What’s your name ?
# def get_full_name(first_name, last_name, middle_name=""):
#     return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"

# print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
# print(get_full_name(first_name="bruce", last_name="lee"))


# Exercise 2 : From English to Morse
#     Write a function that converts English text to morse code and another one that does the opposite.
#     Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
# pass


# # Exercise 3 : Box of stars
# # Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# def box_printer(*args):
#     border = "******************"
#     print(border)
#     for word in args:
#         print(f"* {word:{len(border) - 4}} *") # I don't know why -4, this is just what worked 
#     print(border)

# box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# Exercise 4

#     Analyse this code before executing it. What is the purpose of this code? 
# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

# Answer: List sorting