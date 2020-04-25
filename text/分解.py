import os
import re


def path(filename):
    file = str(os.path.abspath(
        "C:/Users/taiki.NINSAN/Desktop/text/" + filename + ".txt"))
    return file


f = open(path("test"), "r", encoding="utf-8")
line = f.readline()

datas1 = ""
datas2 = ""
datas3 = ""

pattern1 = r".*/.*/.*\(.\)"
pattern2 = r"\d+:\d+\tたいき.*"
pattern3 = r"\d+:\d+\tあ🎂1130🎂新井珠未\[高1-3\].*"
# 集合生成
while line:
    # muching1 = re.search(pattern1, line)
    muching2 = re.search(pattern2, line)
    muching3 = re.search(pattern3, line)
    # if muching1:
    #     datas1 += muching1.group() + "\n"
    if muching2:
        datas2 += muching2.group() + "\n"
    if muching3:
        datas3 += muching3.group() + "\n"
    line = f.readline()

#     datas1 = (re.search(pattern1, line))
f.close()
# print(datas1)
# print(datas2)

# f = open(path("日付"), "w", encoding="utf-8")
# f.write(datas1)
f = open(path("たいき"), "w", encoding="utf-8")
f.write(datas2)
f = open(path("たまみ"), "w", encoding="utf-8")
f.write(datas3)
