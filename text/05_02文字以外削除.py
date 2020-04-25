import os
import re


def path(filename):
    file = str(os.path.abspath(
        "C:/Users/taiki.NINSAN/Desktop/text/" + filename + ".txt"))
    return file


f = open(path("test"), "r", encoding="utf-8")
line = f.readline()

datas1 = ""

# 日付が含まれている場合削除
pattern1 = r"\t.*"

# 集合生成
while line:
    muching1 = re.search(pattern1, line)
    if muching1:
        datas1 += muching1.group() + "\n"
    line = f.readline()

#     datas1 = (re.search(pattern1, line))
f.close()
# print(datas1)
# print(datas2)

f = open(path("名前削除"), "w", encoding="utf-8")
f.write(datas1)
