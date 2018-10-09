import os
import django
import xlrd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FAQ.settings")
django.setup()

if __name__ == "__main__":
    from app.models import PuzzleInfo
    file = xlrd.open_workbook('项目题库.xls')
    sheets = file.sheet_names()
    worksheet = file.sheet_by_name(sheets[0])
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)
        tmp = PuzzleInfo()
        tmp.ptype = worksheet.cell_value(i, 1)
        tmp.ptitle = worksheet.cell_value(i, 2)
        tmp.pa = worksheet.cell_value(i, 3)
        tmp.pb = worksheet.cell_value(i, 4)
        tmp.pc = worksheet.cell_value(i, 5)
        tmp.pd = worksheet.cell_value(i, 6)
        tmp.pkey = worksheet.cell_value(i, 7)
        tmp.pdiff = worksheet.cell_value(i, 8)
        tmp.save()
        # for j in range(0, worksheet.ncols):
        #     print(worksheet.cell_value(i, j), "\t", end="")
        # print()
