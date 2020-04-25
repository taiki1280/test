def plot_graph():
    # y = "1 / 20 * x ** 3"
    import numpy as np
    import matplotlib.pyplot as plt
    lim = 10
    x = np.arange(-lim, lim, 0.1)
    # y = value
    y = eval(change_str())
    # y = exec(value)
    plt.xlim([-lim, lim])  # y軸の表示範囲を -10 から 10 に限定
    plt.ylim([-lim, lim])  # y軸の表示範囲を -10 から 10 に限定
    plt.gca().set_aspect("equal", adjustable="box")  # 方眼紙テクニック
    plt.xlabel("x")  # 横軸のラベル
    plt.ylabel("y",  rotation=0)  # 縦軸のラベル
    plt.grid()  # グリッド（目盛り線）を表示
    plt.plot(x, y)
    plt.savefig("C:/Users/t_kawagishi/Desktop/実験/グラフテスト/figure.png")
    plt.show()


def change_str():
    import re
    text = "y = 3x * *3 +  3x * *2 + 2x"
    text = text.replace(" ", "")
    text = text.replace("y=", "")
    text = text.replace("+", " + ")
    print(text)
    text = re.sub(r"(\d)x", r"\1 * x", text)
    # result = re.search()
    # if result:
    # a = result.group()
    # a = re.sub(r"=", "", a)
    # text = re.sub("y.*=", "", text)
    print(text)
    return text


# change_str()

plot_graph()
