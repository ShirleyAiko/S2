def LookupByProductCode():
    global PCode
    code = int(input("Enter Product Code: "))
    for i in range(len(PCode)):
        if code == PCode[i]:
            return i
        elif i == len(PCode)-1:
            return -1
        else:
            continue

def AddProduct():
    global PCode
    global PDescriptions
    global PRetailPrice
    
    PCode = []
    PDescription = []
    PRetailPrice = []
    
    filehandle = open("PRODUCTS.txt", "r")
    i = 1
    while len(filehandle.readline()) > 0:
        PCode[i] = filehandle.readline()
        PDescription[i] = filehandle.readline()
        Temp = filehandle.readline()
        PRetailPrice[i] = Temp
        i += 1
    filehandle.close()
    print("Product file contents written to arrays")

def LookupByOnline():
    global PCode
    global PDescription
    global PRetailPrice
    
    PCode = []
    PDescription = []
    PRetailPrice = []
    
    filehandle = open("PRODUCTS2.txt", "r")
    lineoftext = filehandle.readline()
    while len(filehandle.readline()) > 0:
        for i in range(len(lineoftext)):
            if lineoftext[i] == ' ' and type(eval(lineoftext[i-1])) == int:
                PCode.append(lineoftext[:i])
                place1 = i+1
            if lineoftext[i-1] == ' ' and type(eval(lineoftext[i])) == int:
                PDescription.append(lineoftext[place1:(i-1)])
                PRetailPrice.append(lineoftext[i:-1])
        lineoftext = filehandle.readline()
    filehandle.close()
    print("Product file contents written to arrays")