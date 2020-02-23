FileHandle = open("qbdata.txt","r")
FileWrite = open("done.txt","w")
LineOfText = FileHandle.readline()
myText = ""
place1 = 0
place2 = 0
while len(LineOfText) > 1:
    s1 = 0
    s2 = 0
    for i in range(len(LineOfText)):
        if LineOfText[i] == ' ':
            s1 += 1
            if s1 == 2:
                place1 = i
    for j in range(len(LineOfText)):
        if LineOfText[j] == ' ':
            s2 += 1
            place2 = j
    myText = str(LineOfText[:place1])+" has a rating of "+str(LineOfText[place2+1:])
    if str(LineOfText[place2+1:-1]) > "60.0":
        FileWrite.write(myText)
        FileWrite.write("\n")
    LineOfText = FileHandle.readline()

FileHandle.close()
FileWrite.close()