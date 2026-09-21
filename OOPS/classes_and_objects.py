class Student():
    # Class Variables - same value for all objects
    school = "Primary School"
    # Instance Variables - different values for different objects

    #constructor
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

    def results(self,english,science,maths):
        total = english + science + maths
        percent_score = total / 300 * 100
        print (total)
        print (percent_score)

student_1 = Student("Samraat", 13, 9)
print (student_1.school)
print(student_1.name)
print(student_1.age)
print(student_1.year)
student_1.results(87,91,69)

student_2 = Student("Emily", 15, 10)
print (student_2.school)
print(student_2.name)
print(student_2.age)
print(student_2.year)
student_2.results(97,78,81)