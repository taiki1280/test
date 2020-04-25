import tkinter as tk
# ボタンの配置を定義 --- (*1)
BUTTONS = [
  ['7', '8', '9', '/'],
  ['4', '5', '6', '*'],
  ['1', '2', '3', '-'],
  ['0', '.', '=', '+']
]

# ボタンイベントの作成関数 --- (*2)
def make_click(ch):
    def click(e):
        print(ch)
        if ch == '=': calc(0); return
        else: disp.insert(tk.END, ch)
    return click

# 計算式を計算 --- (*3)
def calc(e):
    label["text"] = '= ' + str(eval(disp.get()))

# ウィンドウを作成 --- (*4)
win = tk.Tk()
win.title("自作の電卓")
win.geometry("400x400")
# ディスプレイ部分 --- (*5)
disp = tk.Entry(win, font=('', 20), justify="center")
disp.pack(fill='x')
disp.bind('<Return>', calc)
label = tk.Label(win, font=('', 20), anchor="center")
label.pack(fill='x')
# 電卓のボタンを一括作成 --- (*6)
fr = tk.Frame(win)
fr.pack()
for y, cols in enumerate(BUTTONS):
    for x, n in enumerate(cols):
        btn = tk.Button(fr, text=n,
            font=('', 20), width=6, height=3)
        btn.grid(row=y+1, column=x+1)
        btn.bind('<1>', make_click(n))

# ウィンドウを動かす --- (*7)
win.mainloop()
