a_array = ["bbb"]
b_ary = []


def a(value):
    value.append("aaa")


a(b_ary)
print(a_array)
print(b_ary)
