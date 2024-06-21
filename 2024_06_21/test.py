class Student:
    classname = 'My Class'
    def __init__(self):
        pass
print(Student.classname)
student_1 = Student()
Student.classname = "Jack's Class"
print(Student.classname)
print(student_1.classname)
