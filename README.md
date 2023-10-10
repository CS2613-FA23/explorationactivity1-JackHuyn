[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oB7VDeFN)
# ExplorationActivity1

## Question
#### Which package/library does the sample program demonstrate?

#### How does someone run your program?

#### What purpose does your program serve?

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

        Dataframe()

            This function convert a array of data into a Dataframe ( use for multitple data input)

        info()

            Return information of data set (data type, data size, non-null value)

        head()

            Print first 5 data in a data frame/ series
        tail(n)

            Print last 5 data in a data frame/ series

        toString()

            Print everything in the data farme/ series


    Read/Write 

        read_csv
            Load data from CSV file
        read_JSON
            Load data from JSON file
        to_csv 
            Write data to CSV file
        to_JSON
            Write data to JSON file

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
            return boolean value fpr each row
        
        drop_duplicated()



3.  What are the functionalities of the package?/library?

    a  To analyze the data set from JSON, csv or excel file. 
    b  To make a graph, calculate probability, vv

4.  When was it created?

        Pandas was created in January 11 2008

5.  Why did you select this package/library?

        I choose pandas as my topic research because my major is Data Science, this will be my foundation for me future project as well as improve my knowledge when handling data sets problem.

6.  How did learning the package/library influence your learning of the language?

7.  How was your overall experiences with the package/library?

## References
    Basic writing and formatting syntax - GitHub Docs. (n.d.). GitHub Docs. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

    GeeksforGeeks. (2021). How to install Python Pandas on MacOS. GeeksforGeeks. https://www.geeksforgeeks.org/how-to-install-python-pandas-on-macos/

    pandas - Python Data Analysis Library. (n.d.). https://pandas.pydata.org/about/#:~:text=History%20of%20development,make%20open%20source%20pandas%20possible.

    Pandas tutorial. (n.d.). https://www.w3schools.com/python/pandas/default.asp

    CORGIS Datasets Project. (n.d.). https://corgis-edu.github.io/corgis/csv/weather/

    VS Code: ModuleNotFoundError: No module named “pandas.” (n.d.). Stack Overflow. https://stackoverflow.com/questions/63388135/vs-code-modulenotfounderror-no-module-named-pandas

    Download free sample JSON file with multiple records. (n.d.). Hire Developers, Free Coding Resources for the Developer. https://www.appsloveworld.com/download-sample-json-file-with-multiple-records