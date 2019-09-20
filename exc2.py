LeadingNumberOfSpaces = int(input("Enter Leading Number Of Spaces: ")) #MaxNumberOfSymbols of type Integer
Symbol = 'A' #Symbol of type String

MiddleSpaces = -1 #MiddleSpaces of type Integer
LastNumberOfSymbols = LeadingNumberOfSpaces * 2 + 1 #LastNumberOfSymbols of type Integer

while LeadingNumberOfSpaces >= 0:
    
    if MiddleSpaces == -1:
        print(" " * LeadingNumberOfSpaces, end = '')
        print(Symbol)
    elif LeadingNumberOfSpaces != 0:
        print(" " * LeadingNumberOfSpaces, end = '')
        print(Symbol, end = '')
        print(" " * MiddleSpaces, end = '')
        print(Symbol)
    else:
        print(Symbol * LastNumberOfSymbols)

    LeadingNumberOfSpaces -= 1
    MiddleSpaces += 2