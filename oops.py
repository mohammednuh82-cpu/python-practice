# Python OOP Practice

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def study(self):
        print(self.name, "is studying Python")


student1 = Student("Mohammed", 22, "Data Science")
student2 = Student("Ali", 21, "Computer Science")

student1.introduce()

print()

student2.introduce()

print()

student1.study()
student2.study()


# Python OOP - Inheritance

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        print("Name:", self.name)
        print("Course:", self.course)


class DataScienceStudent(Student):

    def study_python(self):
        print(self.name, "is studying Python")


student1 = DataScienceStudent("Mohammed", "Data Science")

student1.introduce()
student1.study_python()