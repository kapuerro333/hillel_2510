class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def change(self,new_grade):
        self.grade = new_grade


    def __str__(self):
        return f"Студент {self.name}, {self.age} років, оцінка: {self.grade}"

my_student= Student('Denis',22,10)

my_student.change(12)
print(my_student)