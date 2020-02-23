FileHandle = open("BookInfo.txt", "r")
LineOfText = FileHandle.readline()
BookNum = 1
while len(LineOfText)>0:
    BookAuthor = ""
    BookTitle = ""
    for i in range(len(LineOfText)):
        if LineOfText[i]!=",":
            BookAuthor += LineOfText[i]
        else:
            BookTitle += LineOfText[i+2:]
            break
    if BookNum < 10:
        Num = "0"+str(BookNum)
        print("#",Num," book author:",BookAuthor,", book title:", BookTitle)
    else:
        print("#",BookNum," book author:",BookAuthor,", book title:", BookTitle)
    BookNum += 1
    LineOfText = FileHandle.readline()
    
FileHandle.close()