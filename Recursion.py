'''1.) Find the maximum number in an array by using recursion.'''
# def maximum(a):
#     if len(a)==1:
#         return a[0]
#     else:
#         return max(a[0], maximum(a[1:]))
    
# a=[13,4,25,6,25,1,75]
# print(maximum(a))

'''2.) Find the power of a number using recursion. Give base and power as parameters to the function.
    a) Test Case 1:
        If base = 2 and power = 3 then output should be 8
    b) Test Case 2:
        If base = -2 and power = 3 then output should be -8
    c) Test Case 3:
        If base = 2 and power = -3 then output should be 0.125
    d) Test Case 4:
        If base = 0 and power = -1 then output should be 0 '''
# def power(base,expo):
#     if expo==0:
#         return 1
#     elif expo<0:
#         if base<1:
#             return ("Can't divide by 0")
#         else:
#             return 1/(power(base,-expo))
#     else: 
#         return base*(power(base,expo-1))

# base,expo=map(int,input().split())
# print(power(base,expo))

'''3.) Find the GCD of two numbers using recursion.'''
# def gcd(n,m):
#     if n==0:
#         return m
#     else:
#         return gcd(m%n,n)
    
# n,m=map(int,input().split())
# print(gcd(n,m))    

'''4.) Convert a number from decimal to binary by using recursion.'''
# def binary(n):
#     if n==0:
#         return "0"
#     elif n==1:
#         return "1"
#     else:
#         return binary(n//2)+str(n%2)
        
# n=int(input())
# print(binary(n),end="")

'''5.) Write a function called productOfArray which takes in an array of numbers and returns the product of them all.'''
# def productOfArray(a):
#     if len(a)==0:
#         return 1
#     else:
#         return a[0]*productOfArray(a[1:])
# a=[6,7,8,9,6,9,0,5]
# print(productOfArray(a))        