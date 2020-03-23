import openpyxl
import os

wb = openpyxl.load_workbook('example.xlsx')

sheet = wb.get_sheet_names('Sheet1')()

sheet["A1"].value

sheet["A1"].value == None

sheet["A1"].value = 42

sheet["A3"].value = 'Hello'

os.chdir("/Users/mac/Desktop")

wb.save('exceeeel.xlsx')

wb.create_sheet(index=0,title="myothersheet")
