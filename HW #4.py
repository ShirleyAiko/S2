FileHandle = open("AS_CS_opt2_gradebook.txt", "r")
myFile = open("AS_CS_opt2_gradebook_ver4.txt", "w")
LineOfText = FileHandle.readline()

while len(LineOfText) > 0:
    names = []
    names.append(LineOfText.split())
    if names[0][0] == 'Daniel':
        names[0][4] = str(int(names[0][4]) * 1.1)
    myFile.write(LineOfText)
    myFile.write("\n")
    LineOfText = FileHandle.readline()
    
FileHandle.close()
myFile.close()