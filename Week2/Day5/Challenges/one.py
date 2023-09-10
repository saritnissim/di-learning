# Exercise 1
# Write a script that inserts an item at a defined index in a list.
def insert_item(item, index, my_list):
    my_list[index] = item
    return my_list

# Exercise 2
# Write a script that counts the number of spaces in a string.
def count_spaces(my_string):
    string_list = list(my_string)
    return string_list.count(" ")

# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.
def count_cases(my_string):
    lowercase = 0
    uppercase = 0
    for char in my_string:
        if char.islower():
            lowercase += 1
        if char.isupper():
            uppercase += 1

    return f"Total lowercase: {lowercase}, Total uppercase: {uppercase}"

# Exercise 4
# Write a function to find the sum of an array without using the built in function:
def my_sum(my_arr):
    sum = 0
    for x in my_arr:
        sum += x
    return sum

# Exercise 5
# Write a function to find the max number in a list
def find_max(my_list):
    max = my_list[0]
    for x in my_list[1:]:
        if x > max:
            max = x
    return max

# Exercise 6
# Write a function that returns factorial of a number
def factorial(my_num):
    result = my_num
    for x in range(1,my_num):
        result = result*x
    return result

# Exercise 7
# Write a function that counts an element in a list (without using the count method):
def list_count(my_list, elem):
    count = 0
    for x in my_list:
        if x == elem:
            count +=1
    return count

# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
import math
def norm(my_list):
    sum_of_squares = 0
    for x in my_list:
        sum_of_squares += x**2
    return math.sqrt(sum_of_squares)

# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)
def is_mono(my_list):
    asc_flag = True
    desc_flag = True

    for i in range(1, len(my_list)):
        if my_list[i-1] > my_list[i]:
            asc_flag = False
        if my_list[i-1] < my_list[i]:
            desc_flag = False

    return asc_flag or desc_flag

# Exercise 10
# Write a function that prints the longest word in a list.
def longest_word(my_list):
    longest = len(my_list[0])
    longest_word = my_list[0]

    for word in my_list[1:]:
        if len(word) > longest:
            longest = len(word)
            longest_word = word

    return longest_word

# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
def separate_alpha_num(my_list):
    alpha = []
    numeric = []
    for x in my_list:
        if isinstance(x, str):
            alpha.append(x)
        if isinstance(x, (int,float)):
            numeric.append(x)
    return alpha, numeric

# Exercise 12
# Write a function to check if a string is a palindrome:
def is_palindrome(str):
    return str == str[::-1]

# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k:
def sum_over_k(sentence, k):
    result = 0 
    words = sentence.split()
    for word in words:
        if len(word) > k:
            result +=1
    return result

# Exercise 14
# Write a function that returns the average value in a dictionary (assume the values are numeric):
def dict_avg(dict):
    sum = 0
    for x in dict.values():
        sum += x
    return sum/len(dict.values())

# Exercise 15
# Write a function that returns common divisors of 2 numbers:
def find_divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def common_div(num1, num2):
    divisors1 = find_divisors(num1)
    divisors2 = find_divisors(num2)

    return [x for x in divisors1 if x in divisors2]

# Exercise 16
def is_prime(num):
    divisors = find_divisors(num)
    if divisors == [1, num]:
        return True
    return False

# Exercise 17
# Write a function that prints elements of a list if the index and the value are even:
def weird_print(my_list):
    result = []
    for key, val in enumerate(my_list):
        if key % 2 == 0 and val % 2 == 0:
            result.append(val)
    return result

# Exercise 18
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
def type_count(**kwargs):
    type_dict = {}
    for val in kwargs.values():
        type_key = str(type(val).__name__)
        if type_key in type_dict:
            type_dict[type_key]
        else:
            type_dict.update({type_key:1})
    return type_dict


# Exercise 19
# Instructions
def my_split(string, char=" "):
    result = []
    start = 0
    for idx, x in enumerate(string):
        if x == char:
            word = string[start:idx]
            start = idx +1
            result.append(word)
    result.append(string[start:])
    return result

# Exercise 20
# Convert a string into password format.
def password(str):
    return '*' * len(str)

print(insert_item("c", 2, ['a','b','w','d']))
print(count_spaces("Today is Thursday."))
print(count_cases("iCE cream is my Favorite"))
print(my_sum([1,5,4,2]))
print(find_max([0,1,3,50]))
print(factorial(4))
print(list_count(['a','a','t','o'],'a'))
print(norm([1,2,2]))
print(is_mono([2,3,3,3]))
print(longest_word(['apples', 'bananas', 'oranges']))
print(separate_alpha_num([1,2, 'a', 'b', 3, 'c']))
print(is_palindrome('John'))
print(sum_over_k("Do or do not there is no try", 2))
print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))
print(common_div(10,20))
print(is_prime(11))
print(weird_print([1,2,2,3,4,5]))
print(type_count(a=1,b='string',c=1.0,d=True,e=False))
print(password("mypassword"))
print(my_split("Today-is-sunday", "-"))
