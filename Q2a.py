NewEmailDetails = open("NewEmailDetails.TXT", "w")
EmailDetails = open("EmailDetails.TXT", "r")
LineOfText = EmailDetails.readline()
while len(LineOfText)> 0:
    LineOfText = "00" + LineOfText
    NewEmailDetails.write(LineOfText)
    NewEmailDetails.write("\n")
    LineOfText = EmailDetails.readline()
NewEmailDetails.close()
EmailDetails.close()