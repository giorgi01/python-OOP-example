class Students:

    lst = []

    def __init__(self, name, surname, age, ects):
        self.name = name
        self.surname = surname
        self.age = age
        self.ects = ects
        Students.lst.append(self.name+" "+self.surname)

    @classmethod
    def students_name(cls):
        print(Students.lst)

    def is_or_not(self):
        if self.ects == 240:
            print(f'{self.name} {self.surname} is a bachelor')


class Subjects:
    def __init__(self, name, ects, grade):
        self.name = name
        self.ects = ects
        self.grade = grade

    def show_credits(self):
        print(f'{self.name}\'s credits:', self.ects)

    def passed_or_not(self):
        if self.grade > 51:
            print(f'Student passed {self.name}')
        else:
            print(f'Student doesn\'t passed {self.name}')


first_student = Students('Giorgi', 'Giorgadze', 23, 240)
second_student = Students('Name', 'Surname', 22, 210)

Students.students_name()
first_student.is_or_not()
second_student.is_or_not()

first_subject = Subjects('History', 5, 77)
second_subject = Subjects('Chemistry', 3, 48)
first_subject.show_credits()
second_subject.show_credits()
first_subject.passed_or_not()
second_subject.passed_or_not()
