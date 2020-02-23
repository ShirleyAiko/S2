Total = 0
ZeroCount = 0
for i in range(100):
    Total += Result[i]
    if Result[i] == 0:
        ZeroCount += 1
Average = Total / 100
print("Average is: ", Average)
print("The number of Zero is: ", ZeroCount)