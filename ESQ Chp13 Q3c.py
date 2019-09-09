Tally = []
for i in range(2):
    Tally.append([])
    for j in range(5):
        if i == 0:
            Tally[i].append("")
        else:
            Tally[i].append(0)
Tally[0][0]="Reading"
Tally[0][1]="computer games"
Tally[0][2]="Sport"
Tally[0][3]="Programming"
Tally[0][4]="TV"
Choice = int(input("Your choice: "))
while Choice != 0:
    Tally[1][Choice-1] += 1
    Choice = int(input("Your choice: "))
for i in range(5):
    print(Tally[0][i],Tally[1][i])