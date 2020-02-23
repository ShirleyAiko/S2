Tally = []
for i in range(5):
    Tally.append(0)
Choice = int(input("Your choice: "))
while Choice != 0:
    Tally[Choice-1] += 1
    Choice = int(input("Your choice: "))
for i in range(5):
    print(Tally[i])
