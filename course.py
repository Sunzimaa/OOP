"""Course class with name and grades."""


class Course:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def __repr__(self):
        return self.name

    def add_grade(self, grade):
        self.grades.append(grade)
    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if len(self.grades) == 0:
            return -1
        else:
            total_grade = 0
            for grade in self.grades:
                total_grade += grade[1]
            average_grade = total_grade / len(self.grades)
            return average_grade
