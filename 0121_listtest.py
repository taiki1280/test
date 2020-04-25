mode_list = ""
mode_array = ["コマンド", "オウムモード", "電卓モード"]
for num in range(1,len(mode_array)):
    if num <= 9:
        head = "0" + str(num)
    else:
        head = str(num)
    mode_list += head + ". " + mode_array[num] + "\n"
print("[コマンド一覧]\n現在のコマンドは、\n" + mode_list + "の" + str(len(mode_array) - 1) + "個です。\n番号は書かずに日本語を入力してください。")