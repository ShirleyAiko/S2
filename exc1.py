symbol = input("Enter symbol: ") #symbol of type String

MaxNumberOfSymbols = int(input("Enter Max Number Of Symbols: ")) #MaxNumberOfSymbols of type Integer
while MaxNumberOfSymbols%2 != 1:
    MaxNumberOfSymbols = int(input("Enter Max Number Of Symbols: "))

NumberOfSpaces = int((MaxNumberOfSymbols - 1)/2) #NumberOfSpaces of type Integer
NumberOfSymbols = 1 #NumberOfSymbols of type Integer

while NumberOfSymbols <= MaxNumberOfSymbols:
    
    for i in range(NumberOfSpaces):
        print(" ", end='')
    
    for i in range(NumberOfSymbols):
        print(symbol, end='')
    
    print("\n")

    NumberOfSpaces -= 1
    NumberOfSymbols += 2