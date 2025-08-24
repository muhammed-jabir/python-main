# Create a program using Hybrid Inheritance for a School Management System:

# Create a base class Person with attributes: name and age.

# Derive a class Student from Person, with an extra attribute roll_no.

# Derive another class Teacher from Person, with an extra attribute subject.

# Create a class TeachingAssistant that inherits from both Student and Teacher.

# It should store both student and teacher details.

# Write a method to display all details of the teaching assistant.





class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print("name is",self.name)
        print("age is",self.age)

    
    

class Student(Person):
    def __init__(self, name, age,roll_num):
        Person.__init__(self,name, age)
        self.roll_num=roll_num

    def show_student(self):
        self.show_person()
        print("roll number is",self.roll_num)

    
class Teacher(Person):
    def __init__(self, name, age,subject):
        Person.__init__(self,name, age)
        self.subject=subject


    def show_teacher(self):
        self.show_person()
        print("subject is",self.subject)

class TeachingAssistant(Student,Teacher):
    def __init__(self, name, age, subject,roll_num):
        Student.__init__(self,name,age,roll_num)
        Teacher.__init__(self,name,age,subject)

 
    def display(self):
        print("teaching assistant details")

        print("name is",self.name)
        print("age is",self.age)
        print("subject is",self.subject)
        print("roll number is",self.roll_num)

name=input("enter your name")
age=int(input("enter your age"))
subject=input("enter your subject")
roll_num=input("enter your roll_num")

      

ob=TeachingAssistant(name,age,subject,roll_num)
ob.display()
ob.show_student()

