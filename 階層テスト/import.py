from a.b.c import print_a


class A:
    def a(self):
        print("a")
        print_a.run(self)

obj = A()
obj.a()