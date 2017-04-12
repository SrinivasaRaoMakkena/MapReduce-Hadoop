sorted = open("sort1.txt","r")   
results = open("reducer_results.txt", "w")   
storeTotal = 0        
oldStore = None    
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  
       continue             

    thisStore, thisSale = datalist
    

    if oldStore and oldStore != thisStore:        
        results.write("{0}\t{1}\n".format(oldStore, storeTotal))
        print("{0}\t{1}\n".format(oldStore, storeTotal))
        oldStore = thisStore;
        storeTotal = 0

    oldStore = thisStore
    if thisSale != None:
        storeTotal += float(thisSale) 

if oldStore != None: 
    results.write("{0}\t{1}\n".format(oldStore, storeTotal))
    print("{0}\t{1}\n".format(oldStore, storeTotal))

sorted.close() 
results.close() 
