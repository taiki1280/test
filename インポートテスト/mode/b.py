def b():
    print("b")
    from . import c


b()
# c.c(self)


# def b():
#     print("b")
#     import c
#     c.c()
# b()
