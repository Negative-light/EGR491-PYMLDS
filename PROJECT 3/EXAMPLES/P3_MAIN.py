#%%
# This project will keep trake of your income
# It will estmate the amount you are taxed and give you an estimated annual income

#%%
# Imports/Constants/Global Vars
from os import stat
import pandas as pd
import numpy as np
import datetime as dt
FILE_NAME= "incomeSheet.xlsx"
INCOME_SHEET = 'INCOME'
STATS_SHEET= 'STATISTICS'
stats = pd.Series([None])
masterDB = pd.DataFrame(columns=['Pay/Hr', 'Hours', 'Net'])
#%%
# 
def check4Excel():
     import os
     return os.path.isfile(FILE_NAME)
# %% Read Excel
def readExcel(filename, sheet):
     xlFile = pd.ExcelFile(filename)
     return pd.read_excel(xlFile,sheet_name=sheet, index_col=0)

# %% Make Data Entry
def makeEntry():
     global masterDB
     date = dt.date.today()
     hrPay = float(input('How Much are you payed/hr?'))
     hrs = float(input('How many hours did you work?'))
     netPay = float(input('How much did you take home?'))
     data = pd.Series([date,hrPay, hrs, netPay], name=str(date), index=['Date','Pay/Hr', 'Hours', 'Net'])
     print(data.to_frame().T)
     if masterDB.empty:
          masterDB = data.to_frame().T.round(2)
     else:
          masterDB = pd.concat([data.to_frame().T, masterDB]).round(2)


# %% Run Calcualtions

def masterCalcs():
     global masterDB
     masterDB['Gross'] = masterDB['Pay/Hr'] * masterDB['Hours']
     masterDB['Deduction'] = masterDB.Gross - masterDB.Net
     masterDB['Deduction%'] = masterDB['Deduction']/masterDB.Gross

def statCalcs():
     global stats
     Idex = pd.MultiIndex.from_tuples([('avg', 'Pay/Hr'),('avg', 'Hours'), ('avg','Deduction%'),('est','Annual Income')])
     avgPayPerHr = masterDB['Pay/Hr'].mean()
     avgHrs = masterDB.Hours.mean()
     avgDed = masterDB['Deduction%'].mean()
     estIncome = ((avgPayPerHr*avgHrs)*(1-avgDed))*(52/2)
     stats = pd.Series([avgPayPerHr, avgHrs, avgDed, estIncome], index=Idex).round(2)
# %% Menu
def menuLogic(u_in):
     global masterDB
     if u_in == '1': # Make New Data Entry
          makeEntry()
     elif u_in =='2': # Make
          print(stats)
     elif u_in == '3':
          print(masterDB)
     elif u_in == '4':
          print('Goodbye')
          return
     else:
          print('Invalid Input')
     
     masterCalcs()
     statCalcs()
     print_menu()

def print_menu():
     global masterDB
     print('Please Select an option')
     print("1. Make a new Entry")
     print("2. View Statistics")
     print("3. Print Data")
     print("4. Exit")
     menuLogic(input())

# %% Welcome/Start
# Welcome
print('Hello and Welcome to The Income Data Manager')
print('Checking for a database')

if check4Excel():
     print('Your database is located loading now')
     xl = pd.ExcelFile(FILE_NAME)
     masterDB = readExcel(FILE_NAME, INCOME_SHEET)
     print('Your Database has been loaded')
     print_menu()
else:
     print('You do not have a database')
     print('Do not worry we will get you started')
     
     makeEntry()
     masterCalcs()
     statCalcs()
     print_menu()

with pd.ExcelWriter(FILE_NAME) as w:
     masterDB.to_excel(w, sheet_name=INCOME_SHEET)
     stats.to_excel(w, sheet_name=STATS_SHEET)
     print("FILES SAVED")
# %%