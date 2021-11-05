class Student(object):
    def __init__(self,name,age,gender,level,grades=None): #__init__ similar to constructor
        self.name=name
        self.age=age
        self.gender=gender
        self.level=level
        self.grades=grades or {}


    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
    
    # Define some students
john = Student("John",12,"male",6,{"math":3.3, "science":5.2}) 
jane = Student("Jane",12,"female",6,{"math":3.5, "science":5.5})  

    # Now we  can get to the grades easily
#print(len(john.grades))   
#print(john.grades.values()) 
print(john.getGPA())
print(jane.getGPA())
    