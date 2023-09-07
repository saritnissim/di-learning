#To do this project, you basically need to create four functions:
def display_board(board):
    for row in board:
        line = " | ".join(row)
        print(line)
        print("*" * len(line))

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            print("You have a row!")
            return True
    
    for col in range(3):
        if all([board[col][0] == player, board[1][col] == player, board[2][col] == player]):
            print("You have a column!")
            return True
    
    if all([board[0][0] == player , board[1][1] == player, board[2][2] == player]) or all([ board[0][2] == player, board[1][1] == player, board[2][0] == player]):
        print("You have a diagnol!")
        return True
      
    return False
            
        

def player_input():
    pass

def play():
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' '],
    ]

    display_board(board)

    players = ["X", "O"]
    while True:
        for player in players:
            print(f"Player {player} enter your move...")
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))

            if board[row][column] == " ":
                board[row][column] = player
                display_board(board)
            else:
                print("That square is taken")
            
            if check_win(board, player):
                print("CONGRATULATIONS " + player)
                return


            if all(cell != " " for row in board for cell in row):
                display_board(board)
                print("It's a tie!")
                break
play()