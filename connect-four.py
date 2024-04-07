
def initialiseBoard():
    for i in range(7):
        row = ["-","-","-","-","-","-","-"]
        board.append(row)
def displayBoard():
    for i in board:
        print('', end="|")
        for _ in i:
            print(_, end="|")
        print()

board = []
playerCount = 1
initialiseBoard()
displayBoard()

while True:
    token = 'X'
    if playerCount % 2 == 0:
        token = 'O'
    choice = int(input("Choose collumn (1-7): "))
    choice -= 1
    for i in range(6, -1, -1):
        if board[i][choice] == '-':
            board[i][choice] = token
            playerCount += 1
            break
        
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and not board[row][col + 3] == '-':
                print("win")
                break

    displayBoard()
