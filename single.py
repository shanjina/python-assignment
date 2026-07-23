class Parent:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Dipa", self.name)
class Dipa(Parent):
    def sound(self):
        print(self.name,"talks")
d = Dipa("Anjina")
d.info()
d.sound()
    