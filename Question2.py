def CheckSensor():
    ID = eval(input("Enter sensor ID: "))
    while ID > 10 or ID < 1 or type(ID) != int:
        ID = eval(input("Enter sensor ID: "))
    temp = GetTemp(ID)
    if temp < LowTemp:
        return "Cold"
    elif LowTemp < temp < HighTemp:
        return "Normal"
    else:
        Alarm()

def GetTemp():
    import random
    return random.uniform(0, 100)