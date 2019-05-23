s='azcbobobegghakl'
occ=0
for i in range(0,len(s)-2,1):
    if s[i:i+3]=='bob':
        occ+=1
print("Number of times bob occurs is:",occ)
