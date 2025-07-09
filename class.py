# Class is a blueprint or template for creating objects.

class Student:
    # A Constructor is automatically called when an object of the class is created.
    def __init__(self,fullname,surname):
        self.fullname = fullname
        self.surname = surname

    def show(self):
        print(f"Name: {self.fullname}, Roll No: {self.surname}")


# Object is an instance of a class.

s1 = Student("Pankaj","Gupta");    
s1.show()