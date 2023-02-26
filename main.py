class Persosn:
  def __init__(self, name):
   self.name = name

class Studend(Person):
  grade = 0
  def study(self):
    self.grade += 1

  def __init__(self):
    super().__init("student")

class Teacher(Person):
  salary = 0
  student = []

student = Student
  
  