def GenerateArray(listofresult):
    for i in range(100):
        import random
        listofresult.append(random.radiant())
    
Result = []
GenerateArray(Result)    
Total = 0
Zero = 0
for i in range(100):
    Total += Result[i]
    if Result[i] == 0:
        Zero += 1
Average = Total / 100
print("Average: ", Average)
print("Zero count: ", Zero)