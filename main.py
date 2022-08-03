def printBoard(grid):
    # Prints grid based on input
    print("---------")
    for i in range(3):
        print("|" + " " + grid[i][0] + " " + grid[i][1] + " " + grid[i][2] + " " + "|")
    print("---------")

def convertStringToArray(moveString):
    moveString = moveString.replace(" ", "")
    return [x for x in moveString]

def convertArrayToInts(array):
    return [int(x) for x in array]

def updateGrid(move, grid, currentPlayer):
    grid[move[0] - 1][move[1] - 1] = currentPlayer
    return grid

def isMoveValid(move, grid):
    try:
        int(move[0]), int(move[1])
    except ValueError:
        print("You should enter numbers!")
        return False
    move = convertArrayToInts(move)
    if (move[0] < 1 or move[0] > 3):
        print("Coordinates should be from 1 to 3!")
        return False
    elif (move[1] < 1 or move[1] > 3):
        print("Coordinates should be from 1 to 3!")
        return False

    if grid[move[0] - 1][move[1] - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return False

    return True

def checkRow(grid):
    for row in range(3):
        if (grid[row][0] != " ") and (grid[row][0] == grid[row][1]) and (grid[row][0] == grid[row][2]):
            return True
    return False

def checkCol(grid):
    for col in range(3):
        if (grid[0][col] != " ") and (grid[col][0] == grid[1][col]) and (grid[0][col] == grid[2][col]):
            return True
    return False

def checkDiag(grid):
    if (grid[0][0] != " ") and (grid[0][0] == grid[1][1]) and (grid[0][0] == grid[2][2]):
        return True
    elif (grid[0][2] != " ") and (grid[0][2] == grid[1][1]) and (grid[0][2] == grid[2][0]):
        return True

    return False

def isWon(grid):
    return checkRow(grid) or checkCol(grid) or checkDiag(grid)

def alternatePlayer(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"

def turn(grid, currentPlayer):
    # Take in move
    isValid = False

    while not isValid:
        playerMove = convertStringToArray(input())
        isValid = isMoveValid(playerMove, grid)

    playerMove = convertArrayToInts(playerMove)
    gameGrid = updateGrid(playerMove, grid, currentPlayer)
    printBoard(gameGrid)
    return gameGrid

def main():

    gameGrid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    printBoard(gameGrid)

    currentPlayer = "X"
    turnCount = 0

    while turnCount < 9:
        gameGrid = turn(gameGrid, currentPlayer)  # Takes in user input, update board
        if isWon(gameGrid):
            print(currentPlayer + " wins")
            break;
        currentPlayer = alternatePlayer(currentPlayer)
        turnCount += 1
    else:
        print("Draw")

main()

