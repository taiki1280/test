f = open("test_tamami" + ".txt", "r", encoding="utf-8")
data_list = []
line = f.readline()
while line:
    data_list.append(line.strip())
    line = f.readline()
f.close()
print("最初のメッセージ：", data_list[0])
print("最後のメッセージ：", data_list[len(data_list) - 1])
