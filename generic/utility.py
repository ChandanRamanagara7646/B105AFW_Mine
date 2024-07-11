import openpyxl

from generic.base_class import BaseClass

class Excel:

    @staticmethod
    def get_data(filepath,sheet_name,row,col):
        try:
            wb=openpyxl.load_workbook(filepath)
            sh=wb[sheet_name]
            val=sh.cell(row,col).value
            if val == None:
                print("Cell value is None")
                val=""
        except Exception as e:
            print(str(e))
            val=""
        return val





