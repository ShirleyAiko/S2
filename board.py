def InitialiseBoard(Board):
    Board=[["_" for i in range(7)] for j in range(6)]
    return Board

def SetUpGame():
    global ThisPlayer
    global GameFinished
    ThisPlayer = 'O'
    GameFinished = False
    
def OutputBoard(Board):
    for Row in range(5, -1, -1):
        for Column in range(7):
            print(Board[Row][Column],end='')
        print("\n")
    
def ThisPlayerMakesMove(Player, Board):
    
    def ColumnNumberValid():
        Valid = False
        if ColumnNumber >= 0 and ColumnNumber <= 6:
            if Board[5][ColumnNumber] == "_":
                Valid = True
        return Valid
        
    def FindNextFreePositionInColumn():
        ThisRow = 0
        while Board[ThisRow][ValidColumn] != "_":
            ThisRow += 1
        return ThisRow
    
    def ThisPlayerChoosesColumn():
        global ColumnNumber
        print("Player", Player, "'s turn")
        ColumnNumber = int(input("Enter a valid column number: "))
        while ColumnNumberValid() == False:
            ColumnNumber = int(input("Enter a valid column number: "))
        return ColumnNumber

    global ValidColumn
    global ValidRow
    ValidColumn = ThisPlayerChoosesColumn()
    ValidRow = FindNextFreePositionInColumn()
    Board[ValidRow][ValidColumn] = Player

def CheckIfThisPlayerHasWon(Board):
    
    def CheckHorizontalLineInValidRow():
        global WinnerFound
        for i in range(4):
            if (Board[ValidRow][i] == ThisPlayer and 
                Board[ValidRow][i+1] == ThisPlayer and
                Board[ValidRow][i+2] == ThisPlayer and
                Board[ValidRow][i+3] == ThisPlayer):
                WinnerFound = True
                break
            else:
                WinnerFound = False

    def CheckVerticalLineInValidColumn():
        global WinnerFound
        if ValidRow == 3 or ValidRow == 4 or ValidRow == 5:
            if (Board[ValidRow][ValidColumn] == ThisPlayer and
                Board[ValidRow-1][ValidColumn] == ThisPlayer and
                Board[ValidRow-2][ValidColumn] == ThisPlayer and
                Board[ValidRow-3][ValidColumn] == ThisPlayer):
                WinnerFound = True
            else:
                WinnerFound = False
    
    def CheckForFullBoard():
        global GameFinished
        BlankFound = False
        ThisRow = 0
        while ThisRow != 6 and BlankFound == False:
            ThisColumn = 0
            while ThisColumn != 7 and BlankFound == False:
                if Board[ThisRow][ThisColumn] == "_":
                    BlankFound = True
                ThisColumn += 1
            ThisRow += 1
        if BlankFound == False:
            print("It is a draw")
            GameFinished = True
    
    global WinnerFound
    global GameFinished
    WinnerFound = False
    CheckHorizontalLineInValidRow()
    if WinnerFound == False:
        CheckVerticalLineInValidColumn()
    if WinnerFound == True:
        GameFinished = True
        print(ThisPlayer, " is the winner")
    else:
        CheckForFullBoard()

def SwapThisPlayer(Player):
    if Player == 'O':
        Player = 'X'
    else:
        Player = 'O'
    return Player

myBoard = []
myBoard = InitialiseBoard(myBoard)
ThisPlayer = ''
GameFinished = None
SetUpGame()

while GameFinished == False:
    ThisPlayerMakesMove(ThisPlayer, myBoard)
    OutputBoard(myBoard)
    CheckIfThisPlayerHasWon(myBoard)
    if GameFinished == False:
        ThisPlayer = SwapThisPlayer(ThisPlayer)