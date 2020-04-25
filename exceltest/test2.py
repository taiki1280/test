import pandas as pd
# a = pd.read_excel("dictionary.xlsx", index_col=1)
text = "コマンド"

MODE_DICT = {}
\

def sheet_to_dict(value):
    sheet = pd.read_excel("dictionary.xlsx", sheet_name=value)
    for row in sheet.values:
        MODE_DICT[row[0]] = row[1], row[2]
        # MODE_DICT["メソッド名"] = row[1]
        # print(f"{row[0]}と{row[1]}")


sheet_to_dict("mode")
a = [a for a in MODE_DICT]

print(a)
# インポート先指定(存在すれば）
if str(MODE_DICT[text][1]) != "nan":
    exec(MODE_DICT[text][1])
# メソッド呼び出し
exec(MODE_DICT[text][0])
# print(a)
