import random

def run(self):
    text = ""
    for i in range(1,11):
        text += str(i) + "回目. " + str(random.randrange(1,7,1)) + "\n"
    self.reply(text)
