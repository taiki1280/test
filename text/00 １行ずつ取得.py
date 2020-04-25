import os
import re


def path(filename):
    file = str(os.path.abspath(
        "C:/Users/taiki.NINSAN/Desktop/text/" + filename + ".txt"))
    return file


f = open(path("test"), "r", encoding="utf-8")

pattern1 = '.*望.*'


datas1 = ""
datas2 = ""
pattern1 = r".*/.*/.*\(.\)"
# 集合生成
line = f.readline()
while line:
    muching = re.search(pattern1, line)
    if muching:
        datas1 += muching.group() + "\n"
    # elif re.search(".*:.*たいき.*", line):
    #     datas2 += re.search(".*たいき.*", line).group() + "\n"
    line = f.readline()
f.close()

print(datas1)
# print(datas2)

print("あ")
