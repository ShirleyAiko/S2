FileHandle = open("qbdata_done2.txt", "r")
LineOfText = FileHandle.readline()

CodeNum = str(input("Enter digit Code: ")) #CodeNum of type String
place = 0 #place of type Integer
found = False #found of type Boolean

while len(LineOfText) > 0:
    
    for i in range(len(LineOfText)):
        if LineOfText[i] == ' ':
            place = i
            break
        
    if LineOfText[:place] == CodeNum:
        found = True

    LineOfText = FileHandle.readline()

if found == False:
    print("NOT found")
else:
    print("found")

FileHandle.close()