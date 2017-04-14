#Problem is Cost of property damage due to storm events.
#Actually we can calculate property damage due to storm events per every year
#from the data set. So that Government can research on that to reduce these
#kind of damages in future by viewing this data.

f = open("Storms.csv","r")  # open file, read-only raw data
o = open("mapper_output1.txt", "w") # open file, write - just our key, value pairs
for line in f:
    #seperate each line using comma(,) delimited
    data = line.strip().split(",")
    if len(data) == 9:
        STATE,YEAR,MONTH,EVENT_TYPE,INJURY_DIRECT,INJURY_INDIRECT,DEATHS_DIRECT,DEATHS_INDIRECT,DAMAGE_PROPERTY = data
        if DAMAGE_PROPERTY != "":
            #Finding the cost which ends with K or M to convert it into integer
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
                
#Closing all files which I have opened(Must)            
f.close()
o.close()
