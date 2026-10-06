# Python OOP - Multilevel Inheritance

class Grandparent:

    def family(self):
        print("Grandparent family")


class Parent(Grandparent):

    def work(self):
        print("Parent works")


class Child(Parent):

    def study(self):
        print("Child studies Python")


child = Child()

child.family()
child.work()
child.study()