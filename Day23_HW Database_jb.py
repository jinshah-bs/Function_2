class Employee:

    def __init__(self):
        super().__init__()
        self.emp_name = ""
        self.emp_number = 0

    def get_employee(self):
        print("The employee name:{} and employee id:{}".format(self.emp_name, self.emp_number))

    def set_employee(self):
        self.emp_name = str(input("Enter the name of the Employee "))
        self.emp_number = int(input("Enter the id for the Employee "))
        self.get_employee()


class Student:

    def __init__(self):
        super().__init__()
        self.student_college = ""
        self.student_degree = ""

    def get_student(self):
        print("The College name of the student:{} and Max degree:{}".format(self.student_college, self.student_degree))

    def set_student(self):
        self.student_college = str(input("Enter the student's college name "))
        self.student_degree = str(input("Enter the Max degree of the student "))
        self.get_student()


class Manager(Employee, Student):

    def __init__(self):
        super().__init__()
        self.manager_position = ""
        self.due_amount = 0

    def get_manager(self):
        print("The Manager position in the company:{} and Due amount:{}".format(self.manager_position, self.due_amount))

    def set_manager(self):
        self.manager_position = str(input("Enter position of the manager "))
        self.due_amount = int(input("Enter due amount remaining for the manager "))
        self.get_manager()


class Scientist(Employee, Student):

    def __init__(self):
        super().__init__()
        self.sci_publication = 0

    def get_scientist(self):
        print("The number of publications owned by the scientist:{}".format(self.sci_publication))

    def set_scientist(self):
        self.sci_publication = int(input("Enter no of publications of the scientist "))
        self.get_scientist()


class Labour(Employee):
    pass


l1 = Labour()
s1 = Scientist()
m1 = Manager()
l1.set_employee()
m1.set_manager()
s1.set_scientist()
s1.set_student()


