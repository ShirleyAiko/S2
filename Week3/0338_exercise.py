def GetInfo():
    while True:
        ID = input("Enter your User ID: ")
        if len(ID) == 5 and "A"<=ID[0]<="Z" and "0000"<=ID[1:]<="9999":
            break
    PreferredName = input("Enter your Preferred Name: ")
    return ID+"*"+PreferredName

def TopLevel():
    Continue = "Y"
    while Continue == "Y":
        Name = GetInfo()
        if Name[0] <= 'M':
            Check = WriteInfo(Name, "File1.txt")
        else:
            Check = WriteInfo(Name, "File2.txt")
        if Check == False:
            return "Disk was full"
        Continue = input("Continue or not(Y or N): ")
