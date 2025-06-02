# Encapsulation is the process of binding data (variables) and methods (functions) that operate on that data into a single unit

class Student:
    def __init__(self, name, age):
        self.__name = name      # private variable
        self.__age = age        # private variable

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Create object
s1 = Student("Amit", 20)

s1.display()
s1.set_age(21)
print("Updated Age:", s1.get_age())
