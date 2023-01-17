"""School class which stores information about courses and students."""
import random


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        if student not in self.students:
            id = random.randint(1, 100)
            while any(school_student.get_id() == id for school_student in self.students):
                id = random.randint(1, 100)
            student.set_id(id)
            self.students.append(student)

    def get_students(self):
        return self.students

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def get_courses(self):
        return self.courses

    def add_student_grade(self, student, course, grade):
        if student in self.students and course in self.courses:
            student.add_grade(tuple([course, grade]))
            course.add_grade(tuple([student, grade]))

    def get_students_ordered_by_average_grade(self):
        for i in range(len(self.students)-1):
            if self.students[i].get_average_grade() < self.students[i + 1].get_average_grade():
                help = self.students[i]
                self.students[i] = self.students[i + 1]
                self.students[i + 1] = help
        return self.students

#    print(sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True))
