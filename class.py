'''OOP: Object-oriented programming (OOP) is like organizing your code by thinking about things as objects. Imagine your code is like a toy box, called "class", and each toy is an object. OOP helps you keep your toys (or objects) organized and easy to play with.'''

class student:
#student is a class.
    # __init__ works as initial.
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

# Gives the info.
print(help(student))

# The super() function is used to give access to methods and properties of a parent or sibling class.

'''The isinstance() function will tell us if an Object is an instance of a class.'''
# isinstance(object, type)

'''The issubclass() function will tell us if a subclass of another.'''
# issubclass(object,subclass)

'''__repr__ method returns a string that represents the object in a way that it can be recreated.'''
#  def __repr__(self):

'''__str__ method returns the user readable string form of an object that can be understood by the end users.'''
# def __str__(self):

'''__add__ method is called when the addition operator ( + ) is used with instances of your custom class.'''
# __add__
# print(int.__add__(1,2))
# print(str.__add__("A","B"))

