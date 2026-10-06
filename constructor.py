# Python OOP - Constructor

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Mohammed", 22, "Data Science")
student2 = Student("Ali", 21, "Computer Science")

student1.show_details()

print()

student2.show_details()