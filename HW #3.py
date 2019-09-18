FileHandle = open("AS_CS_opt2_gradebook.txt", "r")
myFile = open("AS_CS_opt2_gradebook_ver3.txt", "w")
LineOfText = FileHandle.readline()

while len(LineOfText) > 0:
    names = []
    names.append(LineOfText.split())
    myFile.write(LineOfText)
    myFile.write(" ")
    myFile.write(str((int(names[0][4])+int(names[0][9])+int(names[0][14]))/3))
    myFile.write("\n")
    LineOfText = FileHandle.readline()
    
FileHandle.close()
myFile.close()