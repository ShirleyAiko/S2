FileHandle = open("AS_CS_opt2_gradebook.txt", "r")
myFile = open("new-gradebook.txt", "w")
LineOfText = FileHandle.readline()
names = []
names.append(LineOfText.split())
SoFar = names[0][14]
Smallest = SoFar
HisName = ''

while len(LineOfText) > 0:
    SoFar = names[0][14]
    if SoFar <= Smallest:
        Smallest = SoFar
        HisName = names[0]
    LineOfText = FileHandle.readline()
    names = []
    names.append(LineOfText.split())

LineOfText = FileHandle.readline()
FileHandle.seek(0)
LineOfText = FileHandle.readline()

while len(LineOfText) > 0:
    if names[0] != HisName:
        myFile.write(LineOfText)
        myFile.write("\n")
    LineOfText = FileHandle.readline()
    names = []
    names.append(LineOfText.split())
    
FileHandle.close()
myFile.close()