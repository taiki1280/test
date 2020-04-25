import pandas as pd
WORDS_DICT = {"こんにちは": "こんにちは！！"}
ADD_DICT = {"こんばんは": "こんばんは"}
WORDS_DICT.update(ADD_DICT)
a_list = []
for val in WORDS_DICT:
    a_list.append(["000", "たいき", val, WORDS_DICT[val]])
df = pd.DataFrame(
    a_list, columns=["受信", "送信", "ID", "LINE名"]
)
df.to_excel("test.xlsx", sheet_name="test", index=False)
print(df)
