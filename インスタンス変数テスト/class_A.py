class A:
    def __init__(self):
        self.DICT = {"step": 1, "a": "b"}

    def a(self):
        self.a_hensu = "a"
        print(self.a_hensu)
        from Mode.Game import b
        b.run(self)


obj = A()
obj.a()
