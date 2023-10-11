import pandas as pd
import random


# data in a array acess same as normal Ex: dataA[0] = 1
#s  ingle data input
dataA = [1,7,2,3]
# multi data input
dataB = {
    "Games":["League", "MHW", "GTAV","Valorant","CS2"],
    "Ranking":[1,2,3,4,5],
    "Poppulation":[42341234,12341234,12341234,12345123,123412234]
}
###############################################################
#Data Frame (for mutlti data input)
# to get the row we can use .loc[n] where n is the index from 0 to n
# print the MHW value


# we can also label the Data Frame 
# with the label, we can use loc["index"] to get specific value we want
# the different from loc[n] and loc[index] is n get the specific row, while index get the "name"


###############################################################
# Series (used when have a single array of data)
# to make a label, instead of number from 1 to n
# we can specify the label we want (index must match array length)


print("Testing")

mySData = pd.Series(dataA)
myDFdata = pd.DataFrame(dataB)

# you can specific the index of a data set
# the index must match the number of variable
myDFdataB = pd.DataFrame(dataB, index = ["Rank 1","Rank 2","Rank 3","Rank 4","Rank 5"])

print("Some example code: ")
print(mySData)
print(myDFdata)
print(myDFdataB)
###############################################################
# Load data from CSV file

readA = pd.read_csv('weather.csv') 
weatherA = pd.DataFrame(readA)
   
# Load data from JSON file
readB =pd.read_json('EmployeeData.json')
employData = pd.DataFrame(readB)

# set limit to row when display
print("To check the limit row you pc can print, print pd.option.display.max_rows ")
print("You can change the maximum row by pd.options.display.max_rows = n")
pd.options.display.max_rows = 5

print("***********************************************")
print("Example after reading from CSV file ")
print(weatherA)
print("Example after reading from JSON file ")
print(employData)
print("To print the entire CSV file, add .to_string()")
#print(weatherA.to_string())

###############################################################
# Analyzing data


# use .info() to get the information about the data set
# .info will return the Dtype of value
# as well as non-null count which you can see how many value 
# is left blank

print("***********************************************")
print("Analyzing Data:")
print("Analyzing weather data")
print(weatherA.info())
print("***********************************************")
print("Analyzing employee data")
print(employData.info())




# .head() will autotatically print first 5
# line in the data, if you want to specific the number of row
# use .head(n) where n is the bumber you want
# the same go with .tail()





###############################################################
# Manipulating data

# remove empty cells
# we will use dropna() function to return a new DF without empty cells

# to fill in the empty cell with data
# use fillna(130)
# to specifiles column
# ["sth"].fillna(130)

# for both fill and drop, the function will return the new data set
# if you dont want to create the new data set, you can use (inplace = true)



print("***********************************************")
print("Manipulating data")

readC = pd.read_csv('smoking.csv')
smokeData = pd.DataFrame(readC)

print(smokeData.info())

# from the input, the amt_weekends has lots of na/null value
# we can drop the null value by

newData = smokeData.dropna()
print(newData.info())

newDataB = smokeData.fillna(random.randint(1,100))
print(newDataB.info())

mean = weatherA["Data.Temperature.Max Temp"].mean()
median = weatherA["Data.Wind.Speed"].median()
mode = newData["age"].mode()

print("The avg max temp is:\n")
print(mean)
print("The middle value for wind speed :\n")
print(median)
print("Most common age of smoking is: \n")
print(mode)


###############################################################
# Ploting graph
# to be able to graph some data, we must import new library
import matplotlib.pyplot as plot

smokeData.plot(kind="hist",x="age", y="amt_weekdays")
weatherA.plot(kind='scatter',x="Data.Wind.Direction", y="Data.Wind.Speed")
plot.show()


