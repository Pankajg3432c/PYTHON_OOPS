# 1. Single Inheritance

# Parent class (Base class): Jisme original code hota hai.
# Child class (Derived class): Jo parent class se inherit karti hai.

class Parent:
    def speak(self):
        print("Animal Speaks")


class Child(Parent):
    def bark(self):
        print("Dog barks")

c1 = Child()
c1.speak()
c1.bark()   


# 2. Multiple Inheritance

class Father:
    def father_info(self):
         print("Father: Engineer")

class Mother:
    def mother_info(self):
        print("Mother: Doctor")

class Child(Father, Mother):
    def child_info(self):
        print("Child: Student")

c = Child()
c.father_info()
c.mother_info()
c.child_info()


# 3. Multilevel Inheritance

class Grandparent:
    def grandparent_info(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def parent_info(self):
        print("I am Parent")

class Child(Parent):
    def child_info(self):
        print("I am Child")

c = Child()
c.grandparent_info()
c.parent_info()
c.child_info()


# 4. Hierarchical Inheritance

class Parent:
    def show(self):
        print("I am Parent")

class Child1(Parent):
    def display1(self):
        print("I am First Child")

class Child2(Parent):
    def display2(self):
        print("I am Second Child")

c1 = Child1()
c2 = Child2()

c1.show()
c1.display1()

c2.show()
c2.display2()


# 5. Hybrid Inheritance

class A:
    def method_A(self):
        print("A")

class B(A):
    def method_B(self):
        print("B")

class C:
    def method_C(self):
        print("C")

class D(B, C):  # Hybrid of Multilevel + Multiple
    def method_D(self):
        print("D")

d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()
