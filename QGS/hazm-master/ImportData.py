import xlrd

import APISetup
import json
# importing file and using a cell
class_one = xlrd.open_workbook("test.xlsx")
sheet = class_one.sheet_by_index(0)
text = sheet.cell_value(0,0)
# print(text)

