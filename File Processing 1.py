FileHandle = open("qbdata.txt", "r")
myFile = open("qbdata_done.txt", "w")
LineOfText = FileHandle.readline()

myChar = str(input("Enter a character: ")) #myChar of type String

while len(LineOfText) > 0:
    for i in range(len(LineOfText)):
        if LineOfText[i] == " ":
            myFile.write(myChar)
        else:
            myFile.write(LineOfText[i])
    myFile.write("\n")
    LineOfText = FileHandle.readline()

FileHandle.close()
myFile.close()