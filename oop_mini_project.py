# Python OOP - Mini Project

class Student:

    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Mohammed", "Data Science", 85)

student1.show_details()
student1.check_result()