import random

def createBingoBoard():
    board = []
    number = []
    for i in range(9):
        number = []
        number.append(random.randint(1,20))
        number.append(False)
        board.append(number)
    return(board)

def takeTurn(board):
    markable = []
    #addition of the two numbers from dice
    rollTotal = random.randint(1,7) + random.randint(1,7)
    for num in board:
        if(num[0] % rollTotal == 0):
            markable.append(num)
    if(len(markable) > 0):
        if(len(markable) >= 1):
            choice = random.choice(markable)
            ind = board.index(choice)
            board[ind][1] = True
        else:
            board[board.index(markable[0])][1] = True
    return(board)

def rollPercentages():
    rolls = {}
    for i in range(100000):
        rollTotal = random.randint(1,6) + random.randint(1,6)
        if(rollTotal not in rolls):
            rolls[rollTotal] = 1
        else:
            rolls[rollTotal] += 1
    print(rolls)

def checkWin(board):
    Win = False
    markLst = []
    winCombo = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    for num in board:
        if(num[1] == True):
            markLst.append(board.index(num))
    for combo in winCombo:
        matches = 0
        for mark in markLst:
            if(mark in combo):
                matches += 1
        if(matches == 3):
            Win = True
            break
    return Win
     #[1,2,3
    #  4,5,6
     # 7,8,9]
     #all combos:[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]

#compute combination to see total number of combinations you can have for a board
#20!/(9!(11!)) = 167960
#[16, 9, 17, 18, 2, 18, 4, 15, 11](3 turns)
def bestBoard():
    bestCounter = 100
    best = bestBoard = []
    for i in range(100000):
        board = createBingoBoard()
        counter = 0
        while(checkWin(board) == False):
            takeTurn(board)
            counter += 1
            if(counter >= 4):
                break
        if(counter < bestCounter):
            bestCounter = counter
            best = board
    print("This board took " + str(bestCounter) + " turns to win the game")
    for num in best:
        bestBoard.append(num[0])
    print(bestBoard)
if __name__ == '__main__':
    rollPercentages()
    bestBoard()
