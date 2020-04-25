import os


def path(filename):
    file = str(os.path.abspath(
        "C:/Users/taiki.NINSAN/Desktop/text/" + filename + ".txt"))
    return file


# filename = input("ファイル名：")

# 作成
# f = open(path("abc"), "w", encoding="utf-8")
# f.write("トーク履歴や\nｗｗｗ")
# f.close()

# 読み込み
f = open(path("test"), "r", encoding="utf-8")
lines = f.readlines()
f.close()


print(lines)
