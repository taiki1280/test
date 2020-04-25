MODE_ARRAY = [
    ("01", "コマンド","comand"),
    ("02", "command","command"),
    ("03", "管理者モード","admin_mode"),
    ("04", "オウムモード"),
    ("05", "電卓モード"),
    ("06", "計算モード"),
    ("07", "財布モード"),
    ("08", "相談モード"),
    ("09", "特定の言葉モード"),
    ("10", "サイコロモード","dice_mode()")
]

# def command():
# for mode in MODE_ARRAY:
# print(MODE_ARRAY),mode)

#     mode_list = ""
#     for mode in MODE_ARRAY:
#         if mode.index() <= 9:
#             head = "0" + str(mode.index())
#     # for index in range(1, len(MODE_ARRAY)):
#     #     if index <= 9:
#     #         head = "0" + str(index)
#     #     else:
#     #         head = str(index)
#     mode_list += "\n" + head + ". " + MODE_ARRAY[index]
#     reply("現在使用可能なコマンドは" + str(len(MODE_ARRAY) - 1) + "個です。",
#           "「コマンド一覧」\n" + mode_list, "日本語のみを入力してください。", "例）オウムモード")
# command()
