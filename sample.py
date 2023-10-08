import pandas as pd


# data in a array acess same as normal Ex: dataA[0] = 1
#single data input
dataA = [1,7,2,3]
dataB = {
    "Games":["League", "MHW", "GTAV","Valorant","CS2"],
    "Ranking":[1,2,3,4,5],
    "Poppulation":[42341234,12341234,12341234,12345123,123412234]
}
###############################################################
#Data Frame (for mutlti data input)
myDFdata = pd.DataFrame(dataA)
myDFdataB = pd.DataFrame(dataB)
# to get the row we can use .loc[n] where n is the index from 0 to n
# print the MHW value
print("Testing")
print(myDFdataB.loc[1])

# we can also label the Data Frame 
myDFdataC = pd.DataFrame(dataB, index = ["Rank 1","Rank 2","Rank 3","Rank 4","Rank 5"])
# with the label, we can use loc["index"] to get specific value we want
# the different from loc[n] and loc[index] is n get the specific row, while index get the "name"


###############################################################
# Series (used when have a single array of data)
# to make a label, instead of number from 1 to n
# we can specify the label we want (index must match array length)
mySData = pd.Series(dataA)
mySDataB = pd.Series(dataB)
mySDataC = pd.Series(dataA, index = ["first","second","third","etc"])
# We can also has key/value obj in a series
# this is used for small data only
# the key in this case will become the label
dataD = {"Pop": 50, "Ammount": 123, "Text": 11}
mySDataD = pd.Series(dataD)

# this is not working
# myDFdataD= pd.DataFrame(dataD)
# to print a dataD in data frame
dataE = {
    "Names":["Pop","Ammount","Text"],
    "Count":[50,123,11]
}
myDFdataE = pd.DataFrame(dataE)
###############################################################
# Load data from CSV file

readA = pd.read_csv('weather.csv') 
weatherA = pd.DataFrame(readA)
   
# Load data from JSON file
#readB =pd.read_json('someth.json')



###############################################################
# Analyzing data

# use .info() to get the information about the data set
# .info will return the Dtype of value
# as well as non-null count which you can see how many value 
# is left blank





# .head() will autotatically print first 5
# line in the data, if you want to specific the number of row
# use .head(n) where n is the bumber you want
# the same go with .tail()





###############################################################
# Manipulating data
# remove empty cells
# we will use dropna() function to return a new DF without empty cells
# if you dont want to change the original data
# use dropna(inplace = True)

# to fill in the empty cell with data
# use fillna(130, inpalce = True)
# to specifiles column
# ["sth"].fillna(130, inplace = True)





###############################################################
# printing data here
print("Printing Series")
print(mySData)
print(mySDataB)
print(mySDataC)
print(mySDataD)

print("***********************************************")

print("Printing Data Frame")
print(myDFdata)
print(myDFdataB)
print(myDFdataC)
print(myDFdataE)
print("***********************************************")
print("Example after reading from CSV file ")
print(weatherA)
print("To print the entire CSV file, add .to_string()")
print(weatherA.to_string())
print("To check the limit row you pc can print, print pd.option.display.max_rows ")
print("You can change the maximum row by pd.options.display.max_rows = n")
pd.options.display.max_rows = 2
print(weatherA)

