import re

line = r'21:01	たいき	うん'

# .*でなるべく多い文字をマッチするため、12は.*に含まれる
pattern1 = '.*たいき.*'
# .*?でなるべく少ない文字をマッチするため、123は\dにの残る
# pattern2 = '.*?(\d+)'

datas1 = re.search(pattern1, line)
# result2 = re.match(pattern2, content)

if datas1:
    print(datas1.group())
    # output:3

# if result2:
#     print(result2.group(1))
#     # output:123
