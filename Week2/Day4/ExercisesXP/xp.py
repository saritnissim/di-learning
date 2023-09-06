import random
# # Exercise 1 : 
# # Write a function called display_message() that prints one sentence telling everyone what you are learning in this course. Call the function, and make sure the message displays correctly.
# def display_message():
#     print("I am learning to be a full-stack developer")

# display_message()


# # Exercise 2
# # Write a function called favorite_book() that accepts one parameter called title. The function should print a message, such as "One of my favorite books is <title>".
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
# favorite_book("The Alchemist")


# # Exercise 3
# # Write a function called describe_city() that accepts the name of a city and its country as parameters. The function should print a simple sentence, such as "<city> is in <country>".) Give the country parameter a default value.
# def describe_city(city, country="the USA"):
#     print(f"{city} is in {country}")
# describe_city("New York")


# # Exercise 4
# # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# def compare_numbers(num1):
#     num2 = random.randint(1,100)
#     if num2 == num1:
#         print(f"The numbers are the same: {num1} == {num2}")
#     else:
#         print(f"Fail.")
# compare_numbers(24)

# # Exercise 5
# # Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence such as "The size of the shirt is <size> and the text is <text>"
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt("small", "This is me")
# # Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# def make_shirt(size="large", text="I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt() # Make a large shirt with the default message
# make_shirt("medium") # Make medium shirt with the default message
# make_shirt("medium", "This is me again") # Make a shirt of any size with a different message.
# make_shirt(size="medium", text="This is a medium") # Bonus: Call the function make_shirt() using keyword arguments.


# # Exercise 6 
# # Create a function called show_magicians(), which prints the name of each magician in the list.
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians():
#     print(magician_names)
# # Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# def make_great():
#     for i in range(len(magician_names)):
#         magician_names[i] = magician_names[i] + " the Great"

# make_great()
# show_magicians()

# # Exercise 7 
# # Create a function called get_random_temp().This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# # def get_random_temp():
# #     return random.randint(-10,40)

# def get_random_temp(season):
#      # Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#      if season == "summer":
#         return random.randint(33,40)
#      if season == "fall":
#         return random.randint(16,23)
#      if season=="winter":
#          return random.randint(-10,15)
#      if season=="spring":
#          return random.randint(24,32)

# # Create a function called main(). Inside this function, call get_random_temp() to get a temperature, and store its value in a variable. Inform the user of the temperature  eg. “The temperature right now is 32 degrees Celsius.”
# def main(season):
#     temp = get_random_temp(season)
#     print(f"“The temperature right now is {temp} degrees Celsius.”")

#     if temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= temp < 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 16 <= temp < 23:
#         print("Getting warmer, but don't forget layers ")
#     elif 24 <= temp < 32:
#         print("Hot!!")
#     elif 32 <= temp < 40:
#         print("Too hot! Drink plenty")
#     else:
#         pass

# usr_season = input("Which season? ")
# main(usr_season)


# # Exercise 8
# # This project allows users to take a quiz to test their Star Wars knowledge.
# # The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.


# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def ask_questions():
#     losses = 0
#     wrong_answers = [] 
#     wins = 0

#     for item in data:
#         usr_answer = input(item["question"])
#         if usr_answer == item["answer"]:
#             wins += 1
#         else:
#             wrong_answers.append("Your answer: {0}. The correct answer: {1}".format(usr_answer, item["answer"]))
#             losses += 1
        
#         if losses > 3:
#             break
#     print(f"Your score is: {losses} incorrect answers and {wins} correct answers.")
#     print(wrong_answers)
    
#     if losses > 3:
#         play = input(f"Play again. Press P to play")
#         if play =="p":
#             ask_questions()

# ask_questions()
