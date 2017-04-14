#Problem is number of deaths due to storm events.
#Actually we can calculate number of deaths due to storm events per every year
#from the data set. So that Government can research on that to reduce these
#kind of damages in future by viewing this data.

#Open required files
f = open("Storms.csv","r")  # open file, read-only raw data
o = open("mapper_output2.txt", "w") # open file, write - just our key, value pairs
#read first line to neglect the titles like Month, DEATHS_DIRECT  to convert string to int 
f.readline()
for line in f:
    #reading all data using comma delimited as data set is .csv file
    data = line.strip().split(",")
    if len(data) == 9:
        STATE,YEAR,MONTH,EVENT_TYPE,INJURY_DIRECT,INJURY_INDIRECT,DEATHS_DIRECT,DEATHS_INDIRECT,DAMAGE_PROPERTY = data
        if DEATHS_DIRECT != "" and DEATHS_INDIRECT != "":
            #adding both direct deaths and indirect deaths
            print "{0}\t{1}".format(MONTH, int(DEATHS_DIRECT)+int(DEATHS_INDIRECT))
            o.write("{0}\t{1}\n".format(MONTH,DEATHS_DIRECT))
# closing all files is mandatory
f.close()
o.close()
