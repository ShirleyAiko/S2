#Question1
def rand(a):
    import random
    answer = random.uniform(-a, a)
    return answer

names = [['Daniel','Chu',0,0,0],['Julian','Ye',0,0,0],['Lisa','Xu',0,0,0],['Shirley','Zeng',0,0,0],['Nico','Jiang',0,0,0],['Tim','Xing',0,0,0],['James','Liu',0,0,0],['Andy','Zhang',0,0,0],['Cathy','Yang',0,0,0],['Bryan','Shan',0,0,0],['Harry','Fang',0,0,0],['Jack','Jin',0,0,0]]

FileHandle = open("AS_CS_opt2_gradebook.txt", "w")

for i in range(len(names)):
    names[i][2] = "Math Grade " + str(int(90+rand(10))) + " average: 90, "
    names[i][3] = "CS Grade " + str(int(95+rand(5))) + " average: 95, "
    names[i][4] = "Phy Grade " + str(int(88+rand(12))) + " average: 88, "

for i in range(len(names)):
    for j in range(len(names[0])):
        FileHandle.write(names[i][j])
        FileHandle.write(" ")
    FileHandle.write("\n")
    
FileHandle.close()