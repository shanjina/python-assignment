class Student:
    College_name="NCMT"
    def __init__(self, name, age, rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    
    def display(self,mark):
        if mark>50:
            print(f' My name is {self.name} from {self.College_name}, I am {self.age} and my roll no is {self.rollno}')
        else:
            print(f'{self.name}Sorry you are fail')
    @classmethod
    def updateCollege(cls,newcollege):
         cls.College_name = newcollege
    @staticmethod
    def Welcome():
        print("THis run no matter what")
    
st1=Student("Anjina", 18,3)
st1.display(55)
print(st1.College_name)

st2=Student("ram", 19,9)
st2.display(60)
print(st2.College_name)

st2.College_name="Bagmati"
print(st2.College_name)
print(st1.College_name)

Student.updateCollege("kist")
print(st1.College_name)
print(st2.College_name)  

st1.Welcome()