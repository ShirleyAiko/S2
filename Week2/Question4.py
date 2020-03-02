def ISBN13(BookNum):
    Weight = len(BookNum)
    Sum = 0
    for i in range(len(BookNum)):
        if type(BookNum[i]) == int:
            if Weight % 2 == 1:
                Sum += 1 * BookNum
            else:
                Sum += 3 * BookNum
            Weight -= 1
    if Sum%10 != 0:
        return 'Incorrect'
    else:
        return 'Correct'
