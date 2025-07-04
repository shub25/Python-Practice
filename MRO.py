class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(C,B):
    # def show(self):
    #     print("D")
    pass

d = D()
d.show()
