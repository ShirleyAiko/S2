def CheckSum(Byte):
    for i in range(len(Byte)-1):
        Sum = 0
        for j in range(Byte[0]-1):
            Sum += Byte[i][j]
        if Sum % 11 == Byte[i][-1]:
            return 'Correct'
        else:
            return 'Incorrect'
            