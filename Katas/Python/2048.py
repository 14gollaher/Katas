# https://open.kattis.com/problems/2048

rows = 4
columns = 4
board = [[0 for x in range(columns)] for y in range(rows)] 

def main():
    wxyz = input().split()
    board[0][0] = int(wxyz[0])
    board[0][1] = int(wxyz[1])
    board[0][2] = int(wxyz[2])
    board[0][3] = int(wxyz[3])

    wxyz = input().split()
    board[1][0] = int(wxyz[0])
    board[1][1] = int(wxyz[1])
    board[1][2] = int(wxyz[2])
    board[1][3] = int(wxyz[3])

    wxyz = input().split()
    board[2][0] = int(wxyz[0])
    board[2][1] = int(wxyz[1])
    board[2][2] = int(wxyz[2])
    board[2][3] = int(wxyz[3])

    wxyz = input().split()
    board[3][0] = int(wxyz[0])
    board[3][1] = int(wxyz[1])
    board[3][2] = int(wxyz[2])
    board[3][3] = int(wxyz[3])

    direction = int(input().strip())
    
    processDirection(direction)
    printBoard()

def printBoard():
    for r in range(rows):
        print('')
        for c in range(columns):
            print(board[r][c], end=' ')

def processDirection(direction):
    if direction is 0:
        for r in range(rows):
            previousElement = -1
            previousElementColumn = 0
            c = 0
            while c < columns:
                if board[r][c] == 0:
                    c += 1
                elif board[r][c] != previousElement:
                    previousElement = board[r][c]
                    previousElementColumn = c
                    c += 1
                else:
                    board[r][previousElementColumn] = previousElement * 2
                    board[r][c] = 0
                    c2 = previousElementColumn + 1
                    while c2 < columns - 1:
                        board[r][c2] = board[r][c2 + 1]
                        c2 += 1
                    board[r][columns - 1] = 0
                    previousElement = -1
            switchHappened = True
            for i in range (3):
                for c3 in range(columns - 1):
                    if board[r][c3] is 0:
                        board[r][c3] = board[r][c3 + 1]
                        board[r][c3 + 1] = 0
    elif direction is 1:
        for c in range(columns):
            previousElement = -1
            previousElementRow = 0
            r = 0
            while r < rows:
                if board[r][c] == 0:
                    r += 1
                elif board[r][c] != previousElement:
                    previousElement = board[r][c]
                    previousElementRow = r
                    r += 1
                else:
                    board[previousElementRow][c] = previousElement * 2
                    board[r][c] = 0
                    r2 = previousElementRow + 1
                    while r2 < rows - 1:
                        board[r2][c] = board[r2 + 1][c]
                        r2 += 1
                    board[rows - 1][c] = 0
                    previousElement = -1
            for i in range (3):
                for r3 in range(rows - 1):
                    if board[r3][c] is 0:
                        board[r3][c] = board[r3 + 1][c]
                        board[r3 + 1][c] = 0
    elif direction is 2:
        for r in range(rows):
            previousElement = -1
            previousElementColumn = 0
            c = columns - 1
            while c >= 0:
                if board[r][c] == 0:
                    c -= 1
                elif board[r][c] != previousElement:
                    previousElement = board[r][c]
                    previousElementColumn = c
                    c -= 1
                else:
                    board[r][previousElementColumn] = previousElement * 2
                    board[r][c] = 0
                    c2 = previousElementColumn - 1
                    while c2 > 0:
                        board[r][c2] = board[r][c2 - 1]
                        c2 -= 1
                    previousElement = -1
                    board[r][0] = 0
            for i in range (3):
                c3 = columns - 1
                while c3 > 0:
                    if board[r][c3] is 0:
                        board[r][c3] = board[r][c3 - 1]
                        board[r][c3 - 1] = 0
                    c3 -= 1
    elif direction is 3:
        for c in range(columns):
            previousElement = -1
            previousElementRow = 0
            r = columns - 1
            while r >= 0:
                if board[r][c] == 0:
                    r -= 1
                elif board[r][c] != previousElement:
                    previousElement = board[r][c]
                    previousElementRow = r
                    r -= 1
                else:
                    board[previousElementRow][c] = previousElement * 2
                    board[r][c] = 0
                    r2 = previousElementRow - 1
                    while r2 > 0:
                        board[r2][c] = board[r2 - 1][c]
                        r2 -= 1
                    previousElement = -1
                    board[0][c] = 0
            r3 = rows - 1
            for i in range (3):
                while r3 > 0:
                    if board[r3][c] is 0:
                        board[r3][c] = board[r3 - 1][c]
                        board[r3 - 1][c] = 0
                    r3 -= 1
main()
