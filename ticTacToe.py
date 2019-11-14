import random

def printBoard(boardData):
    j = 1
    for row in boardData:
        i = 1
        for val in row:
            print(val, end=" ")
            if i != 3:
                print("|", end=" ")
            i = i + 1
        if j != 3:
            print()
            print("-   -   -")
        j = j + 1
    print()

def assignPlayer():
    while True:
        pToken = input("Pick X or O: ")
        if pToken == 'X' or pToken == 'O':
            break
    if pToken == 'X':
        return pToken, 'O'
    return pToken, 'X'

def moveComp(boardData, freeSpaces, compToken):
    row = col = -1
    move = (row, col)
    while move not in freeSpaces:
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        move = (row, col)
    boardData[row - 1][col - 1] = compToken # -1 bc indexing
    freeSpaces.remove((row, col))
    printBoard(boardData)
    return boardData, freeSpaces

def movePlayer(boardData, freeSpaces, pToken):
    playerMove = input("Player: ").split()
    if (len(playerMove) != 2):
        print("Enter 2 numerical values")
        return False, boardData, freeSpaces
    p_row = playerMove[0]
    p_col = playerMove[1]
    if p_row.isdigit() and p_col.isdigit():
        p_row = int(p_row)
        p_col = int(p_col)
        if (not (1 <= p_row <= 3)) or (not (1 <= p_row <= 3)):
            print("Enter numbers between 1-3 inclusive")
            return False, boardData, freeSpaces
    else:  # if user's input doesn't consist of numbers
        print("Enter numerical values")
        return False, boardData, freeSpaces
    #print(boardData)
    #print(boardData[p_row-1][p_col-1])
    boardData[p_row - 1][p_col - 1] = pToken  # update board data with player's move (-1 bc indexing)
    #print(boardData)
    freeSpaces.remove((p_row, p_col))  # update free spaces after player's move
    printBoard(boardData)
    return True, boardData, freeSpaces

def checkWin(boardData, pToken):
    p_win = compWin = False
    # checking rows
    for row in boardData:
        if row[0] != " " and row[0] == row[1] == row[2]:
            if row[0] == pToken:
                p_win = True
                return p_win, compWin
            else:
                compWin = True
                return p_win, compWin

    # checking columns
    for col in range(0, 3): # col index 0-2 inclusive; checking each column
        if boardData[0][col] != " " and boardData[0][col] == boardData[1][col] == boardData[2][col]:
            if boardData[0][col] == pToken:
                p_win = True
                return p_win, compWin
            else:
                compWin = True
                return p_win, compWin

    # checking diagonals
    # diagonal down to right entries have same row and column index
    if boardData[0][0] != " " and boardData[0][0] == boardData[1][1] == boardData[2][2]:
        if boardData[0][0] == pToken:
            p_win = True
            return p_win, compWin
        else:
            compWin = True
            return p_win, compWin
    # diagonal down to left
    if boardData[0][2] != " " and boardData[0][2] == boardData[1][1] == boardData[2][0]:
        if boardData[0][2] == pToken:
            p_win = True
            return p_win, compWin
        else:
            compWin = True
            return p_win, compWin
    return p_win, compWin

def checkGameOver(boardData, pToken):
    p_win, compWin = checkWin(boardData, pToken)
    if p_win:
        print("You won!")
        return True
    if compWin:
        print("You lost!")
        return True
    return False

def main():
    pToken, compToken = assignPlayer()

    boardData = [[" ", " ", " "]] * 3

    freeSpaces = []
    for row in range(1, 4):
        for col in range(1, 4):
            freeSpaces.append((row, col))

    print("How to Play:")
    print("Enter a row 1-3 and a column 1-3 separated by a space when it is your turn!")
    input("Press enter to start!")
    printBoard(boardData)
    i=1
    while True:
        print(i)
        #print(boardData)
        over = checkGameOver(boardData, pToken)
        if over:
            break
        valid, boardData, freeSpaces = movePlayer(boardData, freeSpaces, pToken)
        #print(boardData)
        if valid:
            boardData, freeSpaces = moveComp(boardData, freeSpaces, compToken)
        i+=1

if __name__ == '__main__':
    main()

