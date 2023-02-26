class Person:
  def __init__(self, name):
   self.name = name


class Student(Person):
  grade = 0
  
  def study(self):
    self.grade += 10

  def __init__(self):
    super().__init__("Student")


class Teacher(Person):
  salary = 0
  student = []

  def worck(self):
    self.salary += 10000

  def __init__(self):
    super().__init__("Teacher")
  
    


student = Student()
print(student.grade)
student.study()
print(student.grade)


teacher = Teacher()
teacher.worck()
print(teacher.salary)