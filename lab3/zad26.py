class Student:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Dodano studenta: {name}.")
        else:
            print("Student już istnieje.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
            print(f"Dodano ocenę {grade} dla studenta {name}.")
        else:
            print("Student nie istnieje.")

students = Student()
students.add_student("Anna")
students.add_grade("Anna", 5)
students.add_grade("Anna", 4)
