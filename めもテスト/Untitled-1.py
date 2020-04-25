f = open("a" + ".txt", "r", encoding="utf-8")
data_list = []
line = f.readline().replace("\\n", "\n").rstrip()
print(line)
while line:
    data_list.append(line)
    print(data_list)
    line = f.readline().replace("\\n", "\n").rstrip()
f.close()
print(data_list[0])
