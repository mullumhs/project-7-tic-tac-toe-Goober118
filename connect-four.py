
board = []

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

initialiseBoard()
displayBoard()
playerCount = 0
while True:
    token = X
    if playerCount % 2 == 0:
        token = O
    playerCount += 1



    
