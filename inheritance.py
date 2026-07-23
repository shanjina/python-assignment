class A:
    def name(self):
        print("A")
class B(A):
    def name(self):
        super().name()
        print("C")
b = B()
b.name()

