import pandas as pd


WORDS_DICT = {}
sheet = pd.read_excel("test.xlsx", sheet_name="test")
for row in sheet.values:
    WORDS_DICT[row[0]] = row[1]
print(WORDS_DICT)


