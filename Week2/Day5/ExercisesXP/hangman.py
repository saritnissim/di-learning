import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

word = random.choice(wordslist) 

    ### YOUR CODE STARTS FROM HERE ###
hangman_stages = [
    """
        -------
        |     |
              |
              |
              |
              |
    """,
    """
        -------
        |     |
        O     |
              |
              |
              |
    """,
    """
        -------
        |     |
        O     |
        |     |
              |
              |
    """,
    """
        -------
        |     |
        O     |
       /|     |
              |
              |
    """,
    """
        -------
        |     |
        O     |
       /|\\    |
              |
              |
    """,
    """
        -------
        |     |
        O     |
       /|\\    |
       /      |
              |
    """,
    """
        -------
        |     |
        O     |
       /|\\    |
       / \\    |
              |
    """
]

def play():
    length = len(word)
    word_guess = ["_" for _ in range(length)]
    print("".join(word_guess) + f"({length} letters)")

    guesses = []
    tries = 0

    while True: 
        print(hangman_stages[tries])
        print("".join(word_guess))
        
        # Check if there is a win
        if word_guess == list(word):
            print("Congratulations. You won!")
            break;
        
        #Check if user tried too many times 
        if tries >= len(hangman_stages)-1:
            print("Game Over")
            return
        
        guess = input("Guess a letter: ")
        
        # Check if the guess was already made
        if guess in guesses:
            print(f"You already guessed '{guess}' before")
            continue
        else:
            guesses.append(guess)
        
        #If the guessed letter is in the word
        if word.find(guess) != -1:
            for id, char in enumerate(word):
                #Update every instance of the letter
                if char == guess:
                    word_guess[id] = guess
        else:
        # If the guess is a failure, increment the tries counter
            tries +=1
        

play()