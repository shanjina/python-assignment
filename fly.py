class Flyer:
    def fly(self):
        return"I can fly!"
class Swimmer:
    def swim(self):
        return"I can swim!"
class Duck(Flyer , Swimmer):
    def quack(self):
        return"Quack!"
donald = Duck()
print(donald.fly())
print(donald.swim())
print(donald.quack())