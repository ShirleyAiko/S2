def SearchFile():
    UserID = input("Enter User ID: ")
    PortID = ""
    TimeDate = ""
    LoginEvents = []
    for i in range(1000):
        for j in range(2):
            LoginEvents[i][j] == ""
            
    FileHandle = open("LoginFile.txt", "r")
    LineOfText = FileHandle.readline()
    while len(LineOfText) > 0:
        if LineOfText[:5] == UserID:
            PortID = LineOfText[5:9]
            TimeDate = LineOfText[9:]
                for i in range(1000):
                    if LoginEvents[i][0] == "":
                        LoginEvents[i][0] = PortID
                        LoginEvents[i][1] = TimeDate
                        break
            break
        else:
            LineOfText = FileHandle.readline()

def ValidatePassword(Pass):
    LowerCase = 0
    UpperCase = 0
    Numeric = 0
    for i in range(len(Pass)):
        if 'a' <= Pass[i] <= 'z':
            LowerCase += 1
        elif 'A' <= Pass[i] <= 'Z':
            UpperCase += 1
        elif '0' <= Pass[i] <= '9':
            Numeric += 1
        else:
            return False
    if LowerCase<2 or UpperCase<2 or Numeric <3:
        return False
    else:
        return True

def CheckSensor():
    SensorID = int(input("Enter Sensor ID: "))
    while SensorID < 1 or SensorID > 10:
        SensorID = int(input("Enter Sensor ID: "))
    Temp = GetTemp(SensorID)
    if Temp < LowTemp:
        return "Cold"
    elif LowTemp <= Temp <= HightTemp:
        return "Normal"
    else:
        Alarm()

def ItemProcess(AddItem, InString):
    RetFlag = False
    if AddItem == "Yes":
        RetFlag = AddToList(InString)
    else:
        RemoveFromList(InString)
    return RetFlag

def AddToText():
    FileHandle = open("ScoreDetails.txt", "a")
    Date = input("Enter Date: ")
    while True:
        MembershipNumber = input("Enter Membership Number: ")
        if MembershipNumber == "":
            return
        Score = input("Enter Score: ")
        while Score < "50" or Score > "99":
            Score = input("Enter Score: ")
        FileHandle.write(MembershipNumber+Date+Score+"/n")
    FileHandle.close()

def Lighten():
    BitMap = [[240, 10, 10, 10, 10, 10, 10, 240],
              [80, 80, 240, 80, 80, 240, 80, 80],
              [80, 80, 240, 80, 80, 240, 80, 80],
              [80, 80, 150, 150, 150, 150, 80, 80],
              [80, 80, 240, 240, 240, 240, 80, 80],
              [80, 80, 150, 150, 150, 150, 80, 80],
              [240, 240, 150, 150, 150, 150, 240, 240],
              [240, 240, 150, 150, 150, 150, 240, 240]]
    for Row in range(8):
        for Column in range(8):
            BitMap[Row][Column] *= 1.1
            if BitMap[Row][Column] > 255:
                return "burnt out"

def ProcessMarks():
    Highest = 0
    Index = 0
    Sum = 0
    for i in range(20):
        Sum += Mark[i]
        if Mark[i] >= Highest:
            Highest = Mark[i]
            Index = i
    Average = Sum/20
    print("The average mark is ", Average, " and the highest mark is ", Highest)
    return Index