a = {"a": ["aa", "c"]}
print(a["a"])

b = a["a"]
b.remove("aa")
a["a"] = b
print(a)

# a = ["a", "b"]
# a.remove("a")
# print(a)
