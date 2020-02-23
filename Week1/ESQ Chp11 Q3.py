RogueValue = -1
Total = 0
Count = 0
Number = int(input("Number: "))
while Number != RogueValue:
    Count += 1
    Total += Number
    Number = int(input("Number: "))
if count > 0:
    Average  = Total / Count
    print(Average)
