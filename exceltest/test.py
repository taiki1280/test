#pandasを読み込む
import pandas as pd

#input file name
input_file_name = 'dictionary.xlsx'

#xls book Open (xls, xlsxのどちらでも可能)
input_book = pd.ExcelFile(input_file_name)

#sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
input_sheet_name = input_book.sheet_names

#lenでシートの総数を確認
num_sheet = len(input_sheet_name)

#シートの数とシートの名前のリストの表示
print("Sheet の数:", num_sheet)
print(input_sheet_name)
