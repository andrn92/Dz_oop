class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mark_student = 0
        self.courses_list = []

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lector:
                lecturer.grades_lector[course] += [grade]
            else:
                lecturer.grades_lector[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = '\nStudent:'
        res += f'\nИмя: {self.name}'
        res += f'\nФамилия: {self.surname}'
        res += f'\nСредняя оценка за домашние задания: {self._get_mark()}'
        str1 = ''
        for i in self.courses_list:
            str1 += i + ', '
        res += f'\nКурсы в процессе изучения: {str1[: -2]}'
        str2 = ''
        for i in self.finished_courses:
            str2 += i + ', ' 
        res += f'\nЗавершенные курсы: {str2[: -2]}'
        return res

    def _get_mark(self):
        lst = []
        counter = 0
        for value in self.grades.values():
            for item in value:
                lst.append(item)
                counter += 1
        for key in self.grades:
            self.courses_list.append(key)
        self.mark_student = round(sum(lst)/counter, 1)
        return self.mark_student
        
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._get_mark() > other._get_mark()     

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lector = {}
        self.mark_lector = 0

    def __str__(self):
        res = '\nLecturer:'
        res += f'\nИмя: {self.name}'
        res += f'\nФамилия: {self.surname}'
        res += f'\nСредняя оценка за лекции: {self._get_mark()}'
        return res

    def _get_mark(self):
        lst = []
        counter = 0
        for value in self.grades_lector.values():
            for item in value:
                lst.append(item)
                counter += 1
        self.mark_lector = round(sum(lst)/counter, 1)
        return self.mark_lector

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._get_mark() < other._get_mark() 

    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = 'Reviewer:'
        res += f'\nИмя: {self.name}'
        res += f'\nФамилия: {self.surname}'
        return res


student_1 = Student('Alex', 'Zubov', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Eric', 'Rubin')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_student(student_1, 'Git', 9) 
reviewer_1.rate_student(student_1, 'Python',7)
reviewer_1.rate_student(student_1, 'Python', 5)
reviewer_1.rate_student(student_1, 'Python', 8)

lecturer_1 = Lecturer('Oleg', 'Karpov')
lecturer_1.courses_attached += ['Python']
student_1.courses_in_progress += ['Python']
student_1.rate_lector(lecturer_1, 'Python', 9)
student_1.rate_lector(lecturer_1, 'Python', 8)
student_1.rate_lector(lecturer_1, 'Python', 6)

print(reviewer_1)
print(lecturer_1)
print(student_1)



