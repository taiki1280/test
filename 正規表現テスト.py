
import re
text = "y = x ** 2 + 2x"
text = text.replace(" ", "")
print(text)
text = re.sub(r"\*\*2", r"²", text)
# text = re.sub(r"\*\*(x|\d+)", r"の\1乗", text)

# text = re.sub("")
# text = re.sub(r"**(\d)", r"の乗", text)

print(text)
text = text.replace("*", "")
text = text.replace("+", " + ")
print(text)
