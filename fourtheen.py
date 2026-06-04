class School:
    school_name="ABC High School"
    def __init__(self,name,grade):
        self.name = name
        self.garde = grade
s1=School("Anjina","A")
s2=School("Hari","B")
print(s1.school_name)
print(s2.school_name)
School.school_name = "Future School"
print(s1.school_name)
print(s2.school_name)
s1.school_name = "Hi School"
print(s1.school_name)
print(s2.school_name)
