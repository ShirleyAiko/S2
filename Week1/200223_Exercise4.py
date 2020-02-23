def BubbleSort():
    global UserNameArray
    n = 100
    NoSwaps = False
    while NoSwaps == False:
        NoSwaps = True
        for i in range(n):
            UserID1 = UserNameArray[i][:6]
            UserID2 = UserNameArray[i+1][:6]
            if UserID1 > UserID2:
                Temp = UserNameArray[i]
                UserNameArray[i] = UserNameArray[i+1]
                UserNameArray[i+1] = Temp
                NoSwaps = False
        n -= 1
        