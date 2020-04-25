RUNNING_ID_DICT = {}
RUNNING_ID = "asddsa"
RUNNING_ID_DICT.setdefault(RUNNING_ID,{"モード" : "デフォルトモード"})
RUNNING_ID_DICT.setdefault(RUNNING_ID,{"電卓モード" : 0})
RUNNING_ID_DICT[RUNNING_ID]["電卓モード"] = {"最後の答え" : 1,"第一ステップ" :"num1_set"}
if "num1_set" in RUNNING_ID_DICT[RUNNING_ID]["電卓モード"]:
    print("a")
print(RUNNING_ID_DICT)