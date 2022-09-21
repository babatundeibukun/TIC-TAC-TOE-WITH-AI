# Tic Tac toe  in python
import random

board = ['' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ''


def printBoard(board):
    print(' ' + board[1]  + " | " + board[2] + " | " + board[3] + "" + "          1 | 2 | 3 ")
    print(' ' + board[4]  + " | " + board[5] + " | " + board[6] + "" + "          4 | 5 | 6 ")
    print(' ' + board[7]  + " | " + board[8] + " | " + board[9] + "" + "          7 | 8 | 9 ")



def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = input('Please enter a number within range 1-9: ')
        try:
            move = int(move)
            if move >0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry , you can not go there, that place is occupied!')
            else:
                print('Please enter a valid number within 1-10')
        except:
            print('Please enter a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == '' and x != 0]
    move = 0
    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move= i
                return move
    # check if corners are open
    cornersopen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersopen.append(i)
    if len(cornersopen) > 0:
        move = selectRandom(cornersopen)
        return move
    # check if center is open
    if 5 in possibleMoves:
        move = 5
        return move
    edgesopen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)
    if len(edgesopen) > 0:
        move = selectRandom(edgesopen)
        return move


def selectRandom(li):
    import random
    length = len(li)
    r = random.randrange(0, length)
    return li[r]


def isBoardFull(board):
    if board.count('') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to TIC TAC TOE')
    printBoard(board)
    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('Sorry , the computer has beaten you!')
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O', move)
                print('Computer placed an "O" in postion', move, ":")
            printBoard(board)
        else:
            print('You won!')
            break

    if isBoardFull(board):
        print('Tie Game!')


main()
