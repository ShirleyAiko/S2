def ProcessArray():
    name = ""
    myFile = open("ClassContact.txt", "w")
    sumfornone = 0
    for i in range(len(ClassList)):
        name = ClassList[i]
        detail = SearchFile(name)
        if detail != "":
            AddToFile(detail, myFile)
        else:
            AddToFile(name+"*No number", myFile)
            sumfornone += 1
    return sumfornone

def SearchFile(Name):
    filehandle = open("StudentContact.txt", "r")
    lineoftext = filehandle.readline()
    found = False
    while lineoftext != 0 and found == False:
        if lineoftext[:len(Name)] == Name:
            found = True
            return lineoftext
        else:
            lineoftext = filehandle.readline()
    if found == False:
        return ""
    
def AddToFile(StringName, FileName):
    filehandle = open(FileName, "w")
    filehandle.write(StringName)
    
def GenerateClassList():
    filehandle = open("ClassList.txt", "r")
    lineoftext = filehandle.readline()
    myList = []
    while len(lineoftext) > 0:
        myList.append(lineoftext[:-3])
        lineoftext = filehandle.readline()
    return myList

ClassList = GenerateClassList()