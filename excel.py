from openpyxl import *
import os

path = "C:\\Users\\祝明洲\\Desktop\\excel"
filenames = os.listdir(path)
for filename in filenames:
    if filename.endswith('.xlsx'):
        print(filename)
        single_path = path + "\\" + filename
        wb = load_workbook(single_path)
        ws = wb.active
        ##这里需注意，我如果删1，2，4列，序号要写1，1，2，按删完前面的列后开始计数
        delrow = [1, 1, 1, 1, 1]
        for i in delrow:
            ws.delete_rows(i)
        wb.save(single_path)