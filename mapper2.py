f = open("Storms.csv","r")  # open file, read-only raw data
o = open("mapper_output.txt", "w") # open file, write - just our key, value pairs
f.readline()
for line in f:  
    data = line.strip().split(",")
    if len(data) == 9:
        STATE,YEAR,MONTH,EVENT_TYPE,INJURY_DIRECT,INJURY_INDIRECT,DEATHS_DIRECT,DEATHS_INDIRECT,DAMAGE_PROPERTY = data
        if DEATHS_DIRECT != "" and DEATHS_INDIRECT != "":
            print "{0}\t{1}".format(MONTH, int(DEATHS_DIRECT)+int(DEATHS_INDIRECT))
            o.write("{0}\t{1}\n".format(MONTH,DEATHS_DIRECT))
f.close()
o.close()
