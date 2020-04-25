results = {}
USER_ID = 123
# word = "ステップ", "参加者"
results.setdefault("RUNNING_ID", {"ステップ": 1})
results["RUNNING_ID"].setdefault("参加者", [])
if USER_ID not in results["RUNNING_ID"]["参加者"]:
    results["RUNNING_ID"]["参加者"].append(USER_ID)

# if
# results[word[0]].setdefault("A", [1, 13])
# results[word[0]].setdefault("B", [1, 13])
# results.setdefault(word[0], {}).append(word)
print(results)
