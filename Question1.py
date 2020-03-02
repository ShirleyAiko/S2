def OddCheck(Byte):
    SumOfOne = 0
    for i in range(len(Byte)):
        if Byte[i] == 1:
            SumOfOne += 1
    if SumOfOne%2 == 1:
        return 'Correct'
    else:
        return 'Incorrect'