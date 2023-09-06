import random
# # Exercise 1
# def get_age(year, month, day):
#     current_year = 2023
#     current_month = 9
#     current_day = 6

#     age = current_year - year
#     if month < current_month or (current_month == month and day<current_day):
#         age -= 1
    
#     return age


# # Create a function can_retire(gender, date_of_birth).

# def can_retire(gender, date_of_birth): 
#     year, month, date = [int(x) for x in date_of_birth.split("/")]
#     print(year, month, date)
#     age = get_age(year, month, date)
#     #  Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).
#     if gender == "m" and age >= 67:
#         print("You can retire")
#         return True
#     elif gender == "f" and age > 62 and date_of_birth[0] > 1947:
#         print("You can retire")
#         return True
#     else: 
#         print("You can't retire")
#         return False

# can_retire("f", "1990/04/23")
# can_retire("m", "1950/01/01")

# # Exercise 2 : Sum
# # Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# # Example:
# # If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
# def number_sum(x):
#     total_sum = 0
#     usr_num = ""
#     for i in range(4):
#         usr_num += str(x)
#         total_sum += int(usr_num)
#     return total_sum
# print(number_sum(3))


# # Exercise 3
# def throw_dice():
#     return random.randint(1,6)

# def throw_until_doubles():
#     count = 0
#     rolls = []
#     while True:
#         x = throw_dice()
#         y = throw_dice()
#         rolls.append((x, y))
#         if x == y: 
#             break;
#         count += 1
#     return rolls, count

# def main():
#     result = []
#     total_count = 0
#     for x in range(100):
#         rolls, count = throw_until_doubles()
#         result.append(rolls)
#         total_count += count
    
#     print(result)
#     print(f"Total throws: {total_count}")
#     print(f"Average throws to reach doubles: {total_count/100}")

# main()
