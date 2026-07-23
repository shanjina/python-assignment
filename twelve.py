<<<<<<< HEAD
class Student:
    def __init__ (self, Name, mark1, mark2, mark3):
     self.name= Name
     self.mark1= mark1
     self.mark2= mark2
     self.mark3= mark3
    def average(self):
        avg = (self.mark1+self.mark2+self.mark3)/3
        print("Name:",self.name)
        print("Average Marks:",avg)
s1= Student("Anjina", 90, 70,60)
=======
class Student:
    def __init__ (self, Name, mark1, mark2, mark3):
     self.name= Name
     self.mark1= mark1
     self.mark2= mark2
     self.mark3= mark3
    def average(self):
        avg = (self.mark1+self.mark2+self.mark3)/3
        print("Name:",self.name)
        print("Average Marks:",avg)
s1= Student("Anjina", 90, 70,60)
>>>>>>> 2296ad6dbbd97f4638b65428c5f1f50b09280a3f
s1.average()