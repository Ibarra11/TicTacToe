
def game():
    markers = [[],[]]
    player = 0
    board = [['','',''] , ['','',''], ['','','']]
    remainingPositions = 9
    hasWon = False

    def init():
        markers[0] = input('Player 1 choose your marker: ').upper()
        markers[1] = input('Player 2 choose your marker: ').upper()

    def placeInputOnBoard(position):
        if position <= 3:
            if board[0][position-1] == '':
                board[0][position - 1] = markers[player]
            else:
                print('The position is already occupied on the board.  Please try again!')
                position = getUserMarkerLocation()
                placeInputOnBoard(position)
        elif position <= 6:
            if board[1][position-4] == '':
                board[1][position-4] = markers[player]
            else:
                print("That space on the board is already occupied")
                position = getUserMarkerLocation()
                placeInputOnBoard(position)
        elif position <= 9:
            if board[2][position-7] == '':
                board[2][position-7] = markers[player]
            else:
                print("That space on the board is already occupied")
                position = getUserMarkerLocation()
                placeInputOnBoard(position)
        else:
            print("Sorry that position is out of range of the board.  Please try again")
            position = getUserMarkerLocation()
            placeInputOnBoard(position)



    def checkGame():
        wonGame = False
        if board[0][0] == markers[player] and board[0][1] == markers[player] and board[0][2] == markers[player]:
            wonGame = True
        elif board[0][0] == markers[player] and board[1][1] == markers[player] and board[2][2] == markers[player]:
            wonGame = True
        elif board[0][2] == markers[player] and board[1][1] == markers[player] and board[2][0] == markers[player]:
            wonGame = True
        elif board[0][0] == markers[player] and board[1][0] == markers[player] and board[2][0] == markers[player]:
            wonGame = True
        elif board[0][1] == markers[player] and board[1][1] == markers[player] and board[2][1] == markers[player]:
            wonGame = True
        elif board[0][2] == markers[player] and board[1][2] == markers[player] and board[2][2] == markers[player]:
            wonGame = True
        elif board[1][0] == markers[player] and board[1][1] == markers[player] and board[1][2] == markers[player]:
            wonGame = True
        elif board[2][0] == markers[player] and board[2][1] == markers[player] and board[2][2] == markers[player]:
            wonGame = True
        return wonGame

    def printBoard(l):
        for row in l:
            colIndex = 0
            for col in row:
                if colIndex < 2:
                    print(col, '|', end="")
                    colIndex += 1
                else:
                    print(col, end="")
            print()
    def getUserMarkerLocation():
        return int(input("Player {} please choose a location to place your marker".format(player + 1)))

    init()
    while remainingPositions > 0:
        pos = getUserMarkerLocation()
        remainingPositions -= 1
        print('-------------------------------------')
        placeInputOnBoard(pos)
        if checkGame() == True:
            hasWon = True
            break
        printBoard(board)
        print('-------------------------------------')
        if player == 0:
            player = 1
        else:
            player = 0

    '''
        If there are no more positions on the board left then check if there isnt a winner.  The check game checks the
        last user to place a marker on the board since
    '''
    if hasWon == True:
        print('Congratulations player ', player + 1, ' you just have won the game')
        printBoard(board)
        print('-------------------------------------')
    elif remainingPositions == 0 and hasWon != True:
        print('The game ended in a tie')
        printBoard(board)
game()
