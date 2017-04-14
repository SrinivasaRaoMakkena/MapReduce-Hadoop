#Problem is Cost of property damage due to storm events.
#Actually we can calculate property damage due to storm events per every year
#from the data set. So that Government can research on that to reduce these
#kind of damages in future by viewing this data.

#Iintermediate outputs(sorted) in MapReduce
sorted = open("sort2.txt","r")   
results = open("reducer_results2.txt", "w")   
damageTotal = 0        
old = None
#reading all lines in sorted file
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  
       continue             

    thisMonth, thisSale = datalist
    

    if old and old != thisMonth:        
        results.write("{0}\t{1}\n".format(old, damageTotal))
        print("{0}\t{1}\n".format(old, damageTotal))
        old = thisMonth;
        damageTotal = 0
#converting string to integer to add all the cost values to reduce output to required values
    old = thisMonth
    if thisSale != None:
        damageTotal += int(thisSale) 

if old != None: 
    results.write("{0}\t{1}\n".format(old, damageTotal))
    print("{0}\t{1}\n".format(old, damageTotal))
#Close all the opened files(Must to work properly)
sorted.close() 
results.close() 
