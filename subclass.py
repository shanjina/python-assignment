class Bird:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"I am a bird named{self.name}")
class FlyMixin:
    def fly(self):
        print(f"{self.name} is flying!")
class SwimMixin:
    def  swim(self):
        print(f"{self.name} is swimming!")
class Duck(Bird, FlyMixin, SwimMixin):
    def __init__(self,name):
        super().__init__(name)
d = Duck("hello Duck")
d.display()
d.fly()
d.swim()

