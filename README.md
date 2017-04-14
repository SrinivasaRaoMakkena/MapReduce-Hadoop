# MapReduce-Hadoop

Our data set is based on Storm events, in which months and in which year the disaster was happened and how much damage has been occured like number of people were dead and cost of damaged property. 

Calculated number of deaths(Direct + Indirect) in each month of the year due to storm events by using
Hadoop Map-reduce algorithm and using Python language.

Calculated amount of property damaged due to storm events in each month of the particular year.


Commands to execute: (local machine)--Running mapper and reducer files individually
-----------------------------------
execfile('filename')

Example: execfile('mapper.py')


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
![Alt Chart Number of deaths vs Month ](https://github.com/SrinivasaRaoMakkena/MapReduce-Hadoop/blob/master/MapReduce1_Correct/graphImage1.PNG?raw=true "Bar Chart of  Number of deaths vs Month")
