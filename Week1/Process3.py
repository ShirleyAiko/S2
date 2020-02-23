def addNewBook():
    FileHandle = open("BookInfo.txt","a")
    AuthorName = input("Please enter author name: ")
    while len(AuthorName) == 0:
        AuthorName = input("Please enter author name: ")
    BookTitle = input("Please enter book title: ")
    while len(BookTitle) == 0:
        BookTitle = input("Please enter book title: ")
    TextWriting = AuthorName+", "+BookTitle+"\n"
    FileHandle.write(TextWriting)
    


def SearchBookByAuthor():
    FileHandle = open("BookInfo.txt","r")
    LineOfText = FileHandle.readline()
    Found = False
    AuthorName = input("Please enter author name: ")
    while len(LineOfText)>0 and Found==False:
        for i in range(len(LineOfText)):
            if LineOfText[i]=="," and LineOfText[:i] == AuthorName:
                Found = True
                return LineOfText[i+2:-2]
        LineOfText = FileHandle.readline()
    if Found == False:
        return "sorry, there is no book by this author."
    
def main():
    myChoice = eval(input("--Add a new book to the text file, press 1\n
                          --Search for books written by a given author, press 2\n
                          --End the program, press 3"))
    while myChoice!=1 or myChoice!=2 or myChoice!=3:
        myChoice = eval(input("--Add a new book to the text file, press 1\n--Search for books written by a given author, press 2\n--End the program, press 3"))
    if myChoice == 1:
        addNewBook()
    elif myChoice == 2:
        SearchBookByAuthor()
    else:
        print("The End")
        
main()