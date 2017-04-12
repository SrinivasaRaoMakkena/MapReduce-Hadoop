f = open("Storms.csv","r")  # open file, read-only raw data
o = open("mapper_output1.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split(",")
    if len(data) == 9:
        STATE,YEAR,MONTH,EVENT_TYPE,INJURY_DIRECT,INJURY_INDIRECT,DEATHS_DIRECT,DEATHS_INDIRECT,DAMAGE_PROPERTY = data
        if DAMAGE_PROPERTY != "":
            if DAMAGE_PROPERTY.endswith("K"):
                DAMAGE = DAMAGE_PROPERTY.replace("K","")            
                DAMAGES = float(DAMAGE)*1000
                print "{0}\t{1}".format(MONTH, DAMAGES)
                o.write("{0}\t{1}\n".format(MONTH,DAMAGES))
            elif DAMAGE_PROPERTY.endswith("M"):
                DAMAGE2 = DAMAGE_PROPERTY.replace("M","")  
                DAMAGES = float(DAMAGE2)*1000000
                print "{0}\t{1}".format(MONTH, DAMAGES)
                o.write("{0}\t{1}\n".format(MONTH,DAMAGES))
                
            
f.close()
o.close()
