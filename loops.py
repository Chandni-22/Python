'''Q-1.) Print 1-100, but run loop till 50~three ways.'''

'''1 way'''
# i=1
# j=1
# while i<=50:
#     print(j)
#     if j%2==0:
#         i+=1
#         j+=1
#     else:
#         j+=1

'''2 way'''
# i=1
# j=1
# while i<=50:
#   print(j)
#   print(j+1)
#   i+=1
#   j+=2

'''3 way'''
# i=1
# j=0
# while i<=50:
#     if i==50:
#         if j!=50:
#             print(j+i)
#             j+=1
#         else:
#             print(j+i)
#             i+=1
#     else:
#         print(i)
#         i+=1

'''Q-2.) Prime Numbers till n.'''
# n=int(input())
# j=1
# count=1
# while count<=n:
#     i,scount=1,0
#     while i<=j//2:
#         if j%i==0:
#             scount+=1
#         i+=1
#     if scount==1:
#         count+=1
#         print(j)
#     j+=1

'''Q-3.) Max from n Numbers.'''
    # n=int(input())
    # max=0
    # i=1
    # while i<=n:
    #     a=int(input())
    #     if a>max:
    #         max=a
    #     i+=1
    # print(max)

'''Q-4.) HCF of n Numbers.'''
# n=int(input())
# hcf=0
# m=1
# i=1
# while i<=n:
#     a=int(input())
#     x=a
#     y=m
#     while x>0:
#         y,x=x,y%x
#     hcf=y
#     m=a
#     i+=1
# print(hcf)

'''Q-5.) Write a program to find the sum of all prime numbers between 1 to n.'''
# n=int(input())
# sum=0
# j=1
# count=1
# while count<=n:
#     i,scount=1,0
#     while i<=(j//2):
#         if j%i==0:
#             scount+=1
#         i+=1
#     if scount==1:
#         count+=1
#         print(j,end=",")
#         sum+=j
#     j+=1
# print()   
# print(f"Sum is {sum}.")

'''Q-6.) Print only the prime factors of a given number n.'''
# n=int(input())
# i=1
# while i<=n:
#     if n%i==0:
#         t=i
#         fac=1
#         count=0
#         while fac<=t:
#             if t%fac==0:
#                 count+=1
#             fac+=1
#         if count==2:
#             print(i)
#     i+=1

'''Q-7.) Print the maximum and the minimum out of n given numbers.'''
# n=int(input())
# i=1
# while i<=n:
#     a=int(input())
#     if i==1:
#         max1=a
#         min1=a
#     else:
#         if a>max1:
#             max1=a
#         if a<min1:
#             min1=a
#     i+=1
# print(max1,",",min1)

'''Q-8.) Find the second max of given n numbers.'''
# n=int(input())
# max=0
# smax=0
# i=1
# while i<=n:
#     x=int(input())
#     if max<x:
#         smax=max
#         max=x
#     else:
#         if x>smax:
#             smax=x
#     i+=1
# print(smax)

'''Q-9.) Find the third max of given N numbers.'''
# n=int(input())
# max=smax=tmax=0
# i=1
# while i<=n:
#     x=int(input())
#     if max<x:
#         tmax=smax
#         smax=max
#         max=x
#     elif x>smax:
#         tmax=smax
#         smax=x
#     else:
#         if x>tmax:
#             tmax=x
#     i+=1
# print(tmax)

# c=1
# i=-2
# sum1=0
# sum2=0
# while c<=5:
#     if c<=3:
#         sum1+=i**2
#         print(i,end=',')
#     else:
#         sum2+=i**2
#         print(i,end=',')
#     c+=1
#     i+=1
# if sum1==sum2:
#     print("Yes")
# else:
#     print("No")