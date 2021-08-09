# Creating CSV Files for Robinhood Options

Use this Python3 application to download list of executed Options from your Robinhood account. Set specific period of time to get options from. This script is useful to easily gather data for an Excel spreadsheet. I customized an Excel spreadsheet (which can be found in this repo) I found from this website: http://www.twoinvesting.com/2016/10/options-tracker-spreadsheet . The link will give more information on how the spreadsheet works and how it can be utilized for keeping track of your options trading.


# How to Set Up Application
  **1) Open Terminal and go to your project directory. Create a Python3 virtual enviroment.**
  
  **2) Install the robin_stocks API. This is used to interact with Robinhood's API.**

        `$ pip3 install robin_stocks`
        
  **3) Install PySimpleGUI; The application's interface is built on this package.**
  
        `$ pip3 install pysimplegui`
        
  **4) Now to run the application:**
  
        `$ python3 createOptionsCSV.py`
        
   **Enter your account username and password in the login window. You will have to enter the verification code if necessary from the terminal window. Once you have succesfully logged in you can set the time period to return options for. This will create a CSV file that returns the specified options orders.**
   
  # Use  Generated CSV Files for importing to Excel Spreadsheet
  
  **1) To import the CSV file in Excel go to Data -> Get External Data -> Import Text File.
  The newly created CSV file will be found in the same folder as the script named selectedOptionsFile.csv **
  
  **2) From the Text Import Wizard window select Delimited and Start import at row 2. Click next.**
    
  **3) Select comma under Delimiters and click next.**
  
  **4) Select the experiation_date column and change the data format to Date and select YMD format. Repeat for the order_created_at column. Click Finish.**
  
  **5)CLick and drag to set the fields from A2-I2. **
  
  **6) Click Properties and fill out the options as done in the screenshot below, then click Finish. **
  
  ![Screenshot](https://github.com/nectariosouzou/RobinHoodOptionsCSVCreator/blob/main/Screen%20Shot%202021-08-09%20at%206.38.33%20PM.png)
  
  **7) The data from the selectedOptionsFile.csv should now populate the table. Select column A and under Data toolbar look for the Stocks button. The current stock price column should show live stock prices.**
  
  
  
  
  
