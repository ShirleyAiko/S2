FileReading = open("BookInfo.txt", "r")
FileWriting = open("BookInfo_new.txt", "w")
LineOfText = FileReading.readline()
BookNum = 1
while len(LineOfText)>0:
    BookAuthor = ""
    BookTitle = ""
    for i in range(len(LineOfText)):
        if LineOfText[i]==" ":
            BookAuthor = ord(LineOfText[i+1])
        elif LineOfText[i]==",":
            BookTitle += LineOfText[i+2:-2]
            break
        else: continue
    if BookNum < 10:
        Num = "0"+ str(BookNum)
        Text = "#"+Num+" book title:"+BookTitle+", number of copies:"+str(BookAuthor)+"\n"
    else:
        Text = "#"+str(BookNum)+" book title:"+BookTitle+", number of copies:"+str(BookAuthor)+"\n"
    FileWriting.write(Text)
    BookNum += 1
    LineOfText = FileReading.readline()
FileReading.close()
FileWriting.close()