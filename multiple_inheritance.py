# Python OOP - Multiple Inheritance

class Father:

    def father_skill(self):
        print("Father: Business")


class Mother:

    def mother_skill(self):
        print("Mother: Teaching")


class Child(Father, Mother):

    def child_skill(self):
        print("Child: Programming")


child = Child()

child.father_skill()
child.mother_skill()
child.child_skill()