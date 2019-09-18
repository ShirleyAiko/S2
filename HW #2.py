FileHandle = open("AS_CS_opt2_gradebook.txt", "r")
myFile = open("AS_CS_opt2_gradebook_ver2.txt", "w")
LineOfText = FileHandle.readline()
s = 1
while len(LineOfText) > 0:
    myFile.write(str(s))
    myFile.write(" ")
    myFile.write(LineOfText)
    myFile.write("\n")
    s += 1
    LineOfText = FileHandle.readline()
    
FileHandle.close()
myFile.close()