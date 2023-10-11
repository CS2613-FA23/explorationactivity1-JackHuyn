[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1

## Question
#### Which package/library does the sample program demonstrate?

    The Library that the sample program will demonsrate will me pandas from python

#### How does someone run your program?

    You can simply run the code from VS Code / Or run it in cmd using python3

#### What purpose does your program serve?

    To analyze some simple data set from some given source

#### What would be some sample input/output?


## Package/ Library Overview
#### Which package/library did you select?
I select the pandas package in python to be my topic research for the first exporation activities

1.  What is the package/library?

        What purpose does it serve?

            The pandas library in python is used for analyzing, cleaning, exploring and manipulating data. So it mainly working with data sets. This library will be helpful for student that chosing Data Science as their major.

2.  How do you use it?

        You can just simply import the pandas from the library after install it.

    To install it?

        If you are using Visual Studio Code, open your terminal then simply type in "pip install pandas" . This will install every package you need to use pandas in python

        If you are using Mac, you have to ensure that you have python3 and pip3 up to date. You can check that by using:
        > python3 --version
        > pip3 --version

        If you want to make sure that your pip3 version run perfectlym you can update it by:
        > pip3 install --upgrade pip
    
        To install pandas, type : > pip3 install pandas in the terminal. 
    
    Some basic function to use when using pandas

        Series()
        
            This function convert a array of data into a Series ( use for single data input )

            Ex: dataA = pandas.Series(sth)

        Dataframe()

            This function convert a array of data into a Dataframe ( use for multitple data input)

            Ex: dataA = pandas.DataFrame(sth)

        info()

            Return information of data set (data type, data size, non-null value)

            print(dataA.info())

        head()

            Print first 5 data in a data frame/ series

            Ex: print(dataA.head())

        tail(n)

            Print last 5 data in a data frame/ series

            Ex: print(dataA.tail())

        to_string()

            Print everything in the data farme/ series

            Ex: print(dataA.to_string())


    Read/Write 

        read_csv

            Load data from CSV file

            Ex: fileA = pandas.read_csv(path/output)
        read_JSON

            Load data from JSON file

            Ex: fileB = pandas.read_json(path/output)
        to_csv 

            Write data to CSV file

            Ex : fileA = pandas.to_csv(path/output)
        to_json

            Write data to JSON file

            Ex : fileB = pandas.to_json(path/output)

    Manipulate data

        dropna()
            Return a new Data Framge that empty all rows that contain null value
        fillna()
            Return a new Data Framge that fill all rows that contain null value with a given value
        
        mean()
            return average of a row/ column
        median()
            return middle value of a row/ column
        mode()
            return most frequenly value of a row/ column

        to_datetime()
        
        loc[n, "sth"] replace a value at row n/ column "sth'

        duplicated() 
            return boolean value for each row
        
        drop_duplicated()
            remove duplicated valur for each row



3.  What are the functionalities of the package?/library?

    a  To analyze the data set from JSON, csv or excel file. 
    b  To make a graph, calculate probability, vv
    c  Mainly for working with data sets

4.  When was it created?

    Pandas was created in January 11 2008

5.  Why did you select this package/library?

    I choose pandas as my topic research because my major is Data Science, this will be my foundation for me future project as well as improve my knowledge when handling data sets problem.

6.  How did learning the package/library influence your learning of the language?

    Exporing pandas help me to understand more about python, it was really fun to study this and manipulate data set that i found.

    The library have more function to explore and I'm planing to explore more about this in the future


7.  How was your overall experiences with the package/library?

    From a scale from 1-10, I'm thinking that I'm around 6-7 at the moment, i need more practice as well as some experiences to manipulate/ understand more function

## References
    Basic writing and formatting syntax - GitHub Docs. (n.d.). GitHub Docs. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

    GeeksforGeeks. (2021). How to install Python Pandas on MacOS. GeeksforGeeks. https://www.geeksforgeeks.org/how-to-install-python-pandas-on-macos/

    pandas - Python Data Analysis Library. (n.d.). https://pandas.pydata.org/about/#:~:text=History%20of%20development,make%20open%20source%20pandas%20possible.

    Pandas tutorial. (n.d.). https://www.w3schools.com/python/pandas/default.asp

    CORGIS Datasets Project. (n.d.). https://corgis-edu.github.io/corgis/csv/weather/

    VS Code: ModuleNotFoundError: No module named “pandas.” (n.d.). Stack Overflow. https://stackoverflow.com/questions/63388135/vs-code-modulenotfounderror-no-module-named-pandas

    Download free sample JSON file with multiple records. (n.d.). Hire Developers, Free Coding Resources for the Developer. https://www.appsloveworld.com/download-sample-json-file-with-multiple-records