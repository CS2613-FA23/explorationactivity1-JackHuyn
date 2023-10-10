import pandas as pd


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
myDFdataB = pd.DataFrame(dataB, index = ["Rank 1","Rank 2","Rank 3","Rank 4","Rank 5"])
###############################################################
# Load data from CSV file

readA = pd.read_csv('weather.csv') 
weatherA = pd.DataFrame(readA)
   
# Load data from JSON file
readB =pd.read_json('EmployeeData.json')
Emp = pd.DataFrame(readB)



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



print("To check the limit row you pc can print, print pd.option.display.max_rows ")
print("You can change the maximum row by pd.options.display.max_rows = n")
pd.options.display.max_rows = 10
###############################################################
# printing data here
print(mySData)
print(myDFdata)
print(myDFdata.loc[1])
print(myDFdataB)
print("***********************************************")
print("Example after reading from CSV file ")
print(weatherA)
print("Example after reading from JSON file ")
print(Emp)
print("To print the entire CSV file, add .to_string()")
print(weatherA.to_string())


