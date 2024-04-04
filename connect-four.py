
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
    displayBoard()





    
