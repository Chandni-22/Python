class student:
    def __init__(self, name, last, age, phone):
        self.name=name
        self.last=last
        self.age=age
        self.phone=phone

    def fullName(self):
        return (self.name+" "+self.last)
    
    def back4(self):
        return (self.age-4)
    
    def deffi(self):
        a=f"{self.name} s full name is {self.name} {self.last} and her age is {str(self.age)}."
        return a
    
student_1=student("Chandni", "Vishwakarma", 20, 9873193222)

print(student_1.fullName())
print(student.back4(student_1))
print(student_1.deffi())    