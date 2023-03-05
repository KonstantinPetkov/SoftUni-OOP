from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


teacher = Teacher()
print(teacher.sleep())
print(teacher.get_fired())
print(teacher.teach())