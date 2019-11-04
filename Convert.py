def sixteen(k):
    if k == 10:
        return "A"
    elif k == 11:
        return "B"
    elif k == 12:
        return "C"
    elif k == 13:
        return "D"
    elif k == 14:
        return "E"
    elif k == 15:
        return "F"
    else:
        return k
    
def convert(m, n, mString):
    theLength = len(mString)
    tenString = 0
    for i in range(theLength):
        tenString += eval(mString[i]) * (m ** (theLength-i-1))
    
    theLength = len(str(tenString))
    nString = ""
    quo = tenString // n
    rem = sixteen(tenString % n)
    while quo > 0:
        nString += str(rem)
        tenString = (tenString - rem) // n
        quo = tenString // n
        rem = sixteen(tenString % n)
    nString += str(rem)
    nString = nString[::-1]
    return nString