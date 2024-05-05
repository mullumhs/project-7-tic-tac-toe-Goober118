def main():

    playerCount = 1
    board = initialiseBoard()
    #Print the board
    displayBoard(board)
    while True:
        playerCount = tokenCheck(board, playerCount)
        displayBoard(board)
        if winCheck(board):
            #Check which player has won
            if playerCount % 2 == 0:
                print("Player O wins!")
            else:
                print("Player X wins!")
            break
        #Check for a draw
        if playerCount == 10:
            print("Draw!")
            break
    while True:
        #Display end menu when player wins or draw occurs
        playAgain = input("Press 1 to play again, press 2 to exit: ")
        if playAgain == '1':
            #Repeat main function
            main()
        elif playAgain == '2':
            #End main function
            break
        else:
            print("Invalid input")

def initialiseBoard():
    
    #Define the board
    board = []
    for i in range(3):
        #Append the rows onto the board
        row = [" - "," - "," - "]
        board.append(row)
    return board

def displayBoard(board):
    
    #Print the guide numbers on top of board
    print("| 1 | 2 | 3 |")
    for i in board:
        
        print('', end="|")
        for _ in i:
            print(_, end="|")
        print()

def tokenCheck(board, playerCount):
    
    token = ' X '
    if playerCount % 2 == 0:
        token = ' O '
    if token == ' X ':
        print("Player X's turn")
    else:
        print("Player O's turn")
    choice_row = int(input("Input a row from 1-3: "))
    choice_row -= 1
    choice_col = int(input("Input a collumn from 1-3: "))
    choice_col -= 1
    if board[choice_row][choice_col] == ' - ':
        board[choice_row][choice_col] = token
        playerCount += 1
    else:
        print("Error, token already placed there")
    return playerCount

def winCheck(board):

    #[row][collumn]
    #Check rows

    # Check first row
    if board[0][0] == board[0][1] == board[0][2] != ' - ':
        return True
    # Check second row
    if board[1][0] == board[1][1] == board[1][2] != ' - ':
        return True
    # Check third row
    if board[2][0] == board[2][1] == board[2][2] != ' - ':
        return True
    
    #Check collumns   

    # Check first collumn
    if board[0][0] == board[1][0] == board[2][0] != ' - ':
        return True
    # Check second collumn
    if board[0][1] == board[1][1] == board[2][1] != ' - ':
        return True
    # Check third collumn
    if board[0][2] == board[1][2] == board[2][2] != ' - ':
        return True

    # Check diagonals

    # Check bottom-to-top diagonal
    if board[2][0] == board[1][1] == board[0][2] != ' - ':
        return True
    if board[0][0] == board[1][1] == board[2][2] != ' - ':
        return True


main()