def main():
        
    playerCount = 1
    board = initialiseBoard()
    displayBoard(board)
    while True:
        playerCount = tokenCheck(board, playerCount)
        displayBoard(board)
        winCheck(board)
    # Your code goes here

def initialiseBoard():
    board = []
    for i in range(3):
        row = [" - "," - "," - "]
        board.append(row)
    return board

def displayBoard(board):
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
    # Check second collumn
    if board[0][1] == board[1][1] == board[2][1] != ' - ':
    # Check third collumn
    if board[0][2] == board[1][2] == board[1][3] != ' - ':

    # Check diagonals

    # Check bottom diagonal
    if board[0][0] == board[0][1] == board[0][2] != ' - ':
    if board[0][0] == board[0][1] == board[0][2] != ' - ':


main()