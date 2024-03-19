'''Q-1.) Make a function to print natural numbers till 10.'''
# def naturalNos(n):
#     if n>0:
#         naturalNos(n-1)
#         print(n,end=",")
# naturalNos(10)

'''Q-2.) Odd-Even function.'''
# def oddEven(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
# oddEven(6)

'''Q-3.) My name function.'''
# def myName():
#     print("Welcome to NavGurukul!!")
#     print("My name is Chandni.")
# myName()

'''Default Argument'''
# def bhawna(n,x=90):
#   print("x =",x)
#   print("n =",n)
# bhawna(7)

'''Keyword and Positioning Argument.'''
# def ans(start, last):
#   print(start,last)
# ans(start=7,last=8)
# ans(start=8,last=7)
# ans(last=9,start=20)

'''Q-4.) Square and Qube.'''
# def square(n):
#   print("Square of",n,"is",n**2)
# square(6)

# def qube(n):
#   print("Qube of",n,"is",n**3)
# qube(6)

'''Q-5.) Add x & y.'''
# def add(x,y):
#     print(f"Add of {x} and {y} is",x+y)
# add(7,3)

'''Q-6.) Fizz-Buzz-Bazz function.'''
# def fizz_buzz(n):
#     if n%2==0 and n%3==0 and n%5==0:
#         print("FizzBuzzBazz")
#     elif n%2==0 and n%3==0:
#         print("FizzBuzz")
#     elif n%2==0 and n%5==0:
#         print("FizzBazz")
#     elif n%3==0 and n%5==0:
#         print("BuzzBazz")
#     elif n%2==0:
#         print("Fizz")
#     elif n%3==0:
#         print("Buzz")
#     elif n%5==0:
#         print("Bazz")
#     else:
#         print(n)
# fizz_buzz(15)