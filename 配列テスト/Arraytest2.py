def a(hennsuu):
    hennsuu = {}
    hennsuu.setdefault("モード", "デフォルトモード")
    hennsuu.setdefault("電卓モード", 0)
    return hennsuu


aa = a("aaa")
bb = a("bbb")
aa["モード"] = "オウムモード"

print(aa)
print(bb["電卓モード"])
