n = open("mapper_output2.txt","r")  
s = open("sort2.txt", "w")
l = n.readline()
lines = n.readlines()
lines.sort()
for line in lines:
        print(line)
        s.write(line)
n.close()
s.close()
