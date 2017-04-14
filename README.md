# MapReduce-Hadoop

Our data set is based on Storm events, in which months and in which year the disaster was happened and how much damage has been occured like number of people were dead and cost of damaged property. 

Calculated number of deaths(Direct + Indirect) in each month of the year due to storm events by using
Hadoop Map-reduce algorithm and using Python language.

Calculated amount of property damaged due to storm events in each month of the particular year.


Commands to execute: (local machine)--Running mapper and reducer files individually
-----------------------------------
execfile('filename')

Example: execfile('mapper.py')

Steps
-----------------------------------
1. We  have Storms.csv file with lot of data

2. Mapper.py---> Took 2 values from data as key value pairs and run this file using command---->"\n"

execfile('Mapper.py')

3. Sort.py-----> Took this mapper output in one file and used it as input to the sort.py and sorted the data in alphabetical order.

execfile('Sort.py')

4. Reducer.py--> Took sort.py output to one file and pushed this as input to reducer.py file--> Yeah, we got final output as key value pairs and it is required one. 

execfile('Reducer.py')

5. We took this output file and visualized using Excel to draw the conclusions easily.

Hadoop Eco System:
-------------------
Installing Cloudera --> importing hadoop virtual os ---> writing the commands using hadoop file system and map reduce will automatially gives output

Map-Reduce Problem01
---------------------------------------------------------------------------------------------------------------------------------------
Mapper: output
--------------
![Alt Mapper output](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce1_Correct/MapperImage.PNG?raw=true "Mapper Output")

Reducer---output
----------------
![Alt Reducer output](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce1_Correct/reducerImage.PNG?raw=true "Reducer Output")

Final Graph: Which tells about visualization of our map reduce problem

![Alt Chart PROPERTY_DAMAGE vs Month ](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce1_Correct/graphImage1.PNG?raw=true "Bar Chart of  PROPERTY_DAMAGE vs Month")

Map-Reduce Problem 02
----------------------------------------------------------------------------------------------------------------------------------------

Mapper--Output
---------------
![Alt Mapper output](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce2_Correct/mapperImage2.PNG?raw=true "Mapper Output")

Reducer--output
----------------
![Alt Reducer output](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce2_Correct/reducerImage2.PNG?raw=true "Reducer Output")

Graph: (Number of Deaths vs Month)
----------------------------------
![Alt Chart Number of deaths vs Month ](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce2_Correct/GraphImage2.PNG?raw=true "Bar Chart of  Number of deaths vs Month")
