MODE_DICT = {}


def sheet_to_dict(value):
    import pandas as pd
    sheet = pd.read_excel("dictionary.xlsx", sheet_name=value)
    for row in sheet.values:
        MODE_DICT[row[0]] = row[1], row[2]


sheet_to_dict("mode")

print([MODE for MODE in MODE_DICT])
