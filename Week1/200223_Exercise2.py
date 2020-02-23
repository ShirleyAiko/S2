def Decrypt1(Lookup, CipherChar):
    Found = False
    Index = 0
    while Found==False and Index < len(Lookup):
        if Lookup[Index] == CipherChar:
            Found = True
            OriginalChar = chr(Index)
        else:
            Index += 1
    if Found == True:
        return OriginalChar
    else:
        return "Not Found"