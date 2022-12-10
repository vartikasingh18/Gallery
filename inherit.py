class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def printname(self):
        print(self.fname, self.lname, self.age) 
class Student(Person):
    pass

p1  = Student("Vartika", "Singh", 20)

p1.printname()


    
