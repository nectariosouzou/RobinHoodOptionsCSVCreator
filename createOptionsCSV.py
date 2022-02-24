import os
import csv
import robin_stocks.robinhood as r
import PySimpleGUI as sg
from datetime import date,datetime


login = ""
#variables for CSV files
columns = ['chain_symbol','expiration_date','strike_price','option_type','side','order_created_at','price','processed_quantity']
order_list = list()
current_time = datetime.now()

#Theme for All GUI windows
sg.theme('Dark Amber')

#Login Window Format
login_info = sg.Text("Please Login Below",size=(50,1))
login_layout = [[login_info],[sg.Text('Username'), sg.InputText()],[sg.Text('Password'), sg.InputText()],[sg.Button("Login")]]
login_window = sg.Window("Robinhood Options CSV Creator", login_layout)

#Main Menu Format
main_text = sg.Text('Enter Dates Below: ')
main_info = sg.Text('   ',size=(50,1))
main_layout = [[main_text],[sg.Text('Month: '), sg.Spin([i for i in range(1,12)], initial_value=1),sg.Text('Day: '), sg.Spin([i for i in range(1,31)], 
    initial_value=1),sg.Text('Year: '), sg.Spin([i for i in range(2010,2023)], initial_value=2021)],[sg.Text('To:')],[sg.Text('Month: '), 
    sg.Spin([i for i in range(1,12)], initial_value=current_time.month),sg.Text('Day: '), sg.Spin([i for i in range(1,31)], 
    initial_value=current_time.day),sg.Text('Year: '), sg.Spin([i for i in range(2010,2023)], initial_value=current_time.year)],[main_info,sg.Button("Create CSV File")],[sg.Button("Logout")]]

main_window = sg.Window("Robinhood Options CSV Creator", main_layout)
main_window_active = False


def create_CSV():
    '''Download option orders from RobinHood and create CSV file of option orders in selected time period.
    '''
    try:
        #Retrieve all options orders from account.
        r.export.export_completed_option_orders('.', file_name='allOptionOrders.csv')

        with open('allOptionOrders.csv', 'r') as updated_csv:
            dict_reader = csv.DictReader(updated_csv)
            updated_list  = list(dict_reader) 
        
        for option in updated_list:
           
            create_date = date(int(option['order_created_at'][0:4]),int(option['order_created_at'][5:7]),int(option['order_created_at'][8:10]))
            exp_date = date(int(option['expiration_date'][0:4]),int(option['expiration_date'][5:7]),int(option['expiration_date'][8:10]))
            
            if create_date > date(main_values[2],main_values[0],main_values[1]) and create_date < date(main_values[5],main_values[3],main_values[4]) :
                print(create_date)
                order_list.append([option['chain_symbol'],exp_date,option['strike_price'],option['option_type'],option['side'],create_date,option['price'],option['processed_quantity']])
        
        with open('selectedOptionsFile.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(columns)
            order_list.reverse()
            write.writerows(order_list)
            f.close()
            main_info("Files Created.")
    except:
        main_info("Error Creating CSV File.")
    order_list.clear()
    updated_list.clear()


'''End program if user closes window or presses Login button and continues with program.
'''
while True:
    login_event, login_values = login_window.read()
    if login_event == "Login":
        login_info('Check Terminal to enter Verification Code.')
        username = login_values[0]
        password = login_values[1]
        
        try:
            login = r.login(username,password,expiresIn=86800)
            
            if login['detail'] == 'logged in with brand new authentication code.':
                login_window.close()
                main_window_active = True
        except:
            login_info("Please Try Again. Error Logging In.")
    if login_event == sg.WIN_CLOSED:
        login_window.close()
        break
        
'''If login was succesful get sent to main menu.
'''
if main_window_active == True:
    while True:
        main_event,main_values = main_window.read()
        
        if main_event == "Create CSV File":
            create_CSV()

        if main_event == sg.WIN_CLOSED or main_event == "Logout":
                main_window.close()
                r.logout()
                break