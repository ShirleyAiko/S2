FileRead = open("hamlet.txt", "r")
FileWrite = open("hamletwds.txt", "w")
txt = FileRead.read()
myDict = { }

def space(text):
    for i in "`~!@#$%^&*()_+-=|}{[]\":;'<>?,./" :
        text = text.replace(i, " ")
    return text

wds = (space(txt).lower()).split()

for i in wds:
    myDict[i] = myDict.get(i, 0) + 1

myList = list(myDict.items())
myList.sort(key = lambda x:x[1], reverse = True)

s = 0
for i in range(len(myList)):
    s += myList[i][1]

for i in range(len(myList)):
    FileWrite.write(str(myList[i][0]))
    FileWrite.write(" ")
    FileWrite.write(str(myList[i][1]*100/s))
    FileWrite.write("%")
    FileWrite.write("\n")

FileRead.close()
FileWrite.close()