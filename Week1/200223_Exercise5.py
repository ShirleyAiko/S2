def FindRepeats():
    global UserNameArray
    Count = 0
    for i in range(100):
        if UserNameArray[i][:6] == UserNameArray[i+1][:6]:
            print(UserNameArray[i+1][:6])
            Count += 1
    OutString = "There are"+Count+"repeated UserIDs"
    return OutString