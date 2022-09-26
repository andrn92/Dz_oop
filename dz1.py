class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
       

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
 
mentor_1 = Mentor('Some', 'Buddy')
mentor_1.courses_attached += ['Python']
 
mentor_1.rate_student(student_1, 'Python', 9)
mentor_1.rate_student(student_1, 'Python', 7)
mentor_1.rate_student(student_1, 'Python', 6)
 
print(student_1.grades)    


