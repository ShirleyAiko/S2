InputByte = [[1,0,1,0,0,1,1,1],
           [0,1,1,0,0,0,1,0],
           [1,0,1,1,0,1,0,0],
           [0,0,1,1,0,0,0,0],
           [0,1,1,0,0,1,0,0],
           [0,1,1,0,0,0,1,0],
           [0,1,1,0,0,0,1,0],
           [1,1,0,1,0,1,1,0]]

"""
           
InputByte = [[1,0,1,0,0,1,1],
           [0,1,1,0,0,0,1],
           [1,0,1,1,0,"0",0],
           [0,0,1,1,"1",0,0],
           [0,1,1,0,0,1,0],
           [0,1,1,0,0,0,1],
           [0,1,1,0,0,0,1]]

"""

def CheckRow(Byte):
    ListRowOfError = []
    for i in range(len(Byte)-1):
        SumOfOne = 0
        for j in range(len(Byte[0])):
            if Byte[i][j] == 1:
                SumOfOne += 1
        if SumOfOne%2 !=1:
            ListRowOfError.append(i)
    return ListRowOfError

def CheckColumn(Byte):
    ListColumnOfError = []
    for i in range(len(Byte[0])):
        SumOfOne = 0
        for j in range(len(Byte),1,-1):
            if Byte[j][i] == 1:
                SumOfOne += 1
        if SumOfOne%2 != 1:
            ListColumnOfError.append(i)
    return ListColumnOfError

def Correction(Byte):
    WrongRow = CheckRow(Byte)
    WrongColumn = CheckRow(Byte)

    for i in range(len(WrongRow)):
        x = WrongRow[i]
        y = WrongColumn[i]
        if Byte[x][y] == 1:
            Byte[x][y] = 0
        else:
            Byte[x][y] = 1
    
    return(Byte)

Correction(InputByte)
