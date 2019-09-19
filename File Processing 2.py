FileHandle = open("qbdata.txt", "r")
myFile = open("qbdata_done2.txt", "w")
LineOfText = FileHandle.readline()

name = str(input("Enter name: ")) #name of type String
place = 0 #place of type Integer
CodeNum = 1 #CodeNum of type Integer

def fourdigit(myNum):
    lens = len(myNum) #lens of type Integer
    myNum = "0"*(4-lens) + myNum #myNum of type String
    return myNum

while len(LineOfText) > 0:
    s = 0 #s of type Integer
    for i in range(len(LineOfText)):
        if LineOfText[i] == ' ':
            s += 1
            if s == 2:
                place = i
    if LineOfText[:place] != name:
        myFile.write(fourdigit(str(CodeNum)) + " ")
        myFile.write(LineOfText)
        myFile.write("\n")
    else:
        CodeNum -= 1
        
    CodeNum += 1
    LineOfText = FileHandle.readline()

FileHandle.close()
myFile.close()