'''OOP: Object-oriented programming (OOP) is like organizing your code by thinking about things as objects. Imagine your code is like a toy box, called "class", and each toy is an object. OOP helps you keep your toys (or objects) organized and easy to play with.'''

class student:
#student is a class.
    def __init__(self, name, last, age, phone):
        self.name=name
        self.last=last
        self.age=age
        self.phone=phone
        #self is an object in student.

    def fullName(self):
        return (self.name+" "+self.last)
    
    def back4(self):
        return (self.age-4)
    
    def deffi(self):
        a=f"{self.name} s full name is {self.name} {self.last} and her age is {str(self.age)}."
        return a
    
 #student_1 is an instance of class student.   
student_1=student("Chandni", "Vishwakarma", 20, 9873193222)

print(student_1.fullName())
print(student.back4(student_1))
print(student_1.deffi()) 

#__dict__ will return the dictionary contains the information of instance.
print(student_1.__dict__)  
