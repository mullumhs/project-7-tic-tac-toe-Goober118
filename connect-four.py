


def initialiseBoard():
    board = []
    for i in range(6):
        row = ["-","-","-","-","-","-","-"]
        board.append(row)
    return board

def displayBoard(board):
    print("|1|2|3|4|5|6|7|")
    for i in board:
        print('', end="|")
        for _ in i:
            print(_, end="|")
        print()

def horizontalWinCheck(board):
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and not board[row][col + 3] == '-':
                print("win")
                break

def verticalWinCheck(board):
     for col in range(7):
         for row in range (4):
             if board[col][row] == board[col][row + 1] == board[col][row + 2] == board
def tokenCheck(board, playerCount):
        token = 'X'
        if playerCount % 2 == 0:
            token = 'O'
        choice = int(input("Choose collumn (1-7): "))
        choice -= 1
        for i in range(5, -1, -1):
            if board[i][choice] == '-':
                board[i][choice] = token
                playerCount += 1
                return playerCount

def main():

    playerCount = 1         
    board = initialiseBoard()
    displayBoard(board)
    while True:
        playerCount = tokenCheck(board, playerCount)
        horizontalWinCheck(board)
        displayBoard(board)

main()