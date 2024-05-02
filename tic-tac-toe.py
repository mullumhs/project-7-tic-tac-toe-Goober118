def main():
        
        playerCount = 1
        board = initialiseBoard()
        displayBoard(board)
        while True:
            playerCount = tokenCheck(board, playerCount)
            displayBoard(board)
    # Your code goes here

def initialiseBoard():
    board = []
    for i in range(3):
        row = ["_","_","_"]
        board.append(row)
    return board

def displayBoard(board):
    print("|1|2|3|")
    for i in board:
        print('', end="|")
        for _ in i:
            print(_, end="|")
        print()

def tokenCheck(board, playerCount):
    
    token = 'X'
    if playerCount % 2 == 0:
        token = 'O'
    choice_row = int(input("Input a row from 1-3: "))
    choice_row -= 1
    choice_col = int(input("Input a collumn from 1-3: "))
    choice_col -= 1
    for i in range(2,-1,-1):
        if board[choice_row][choice_col] == '-':
            board[choice_row][choice_col] = token
            playerCount += 1
            return playerCount


main()