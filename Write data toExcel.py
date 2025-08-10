import openpyxl

file = "D:\TestData.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active    #Gets acive sheet in a workbook

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(r,c).value = "Welcome"

workbook.save(file)