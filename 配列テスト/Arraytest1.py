results = []
# words = ["モード選択",]
words_a = ["apple", "beta", "apple", "orange", "alpha"]

for word in words_a:
    if word not in results:
        results.append(word)
print(results)
