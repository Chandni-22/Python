'''Q-1.) Write a program to create an array of natural numbers till 20 and print it.'''
# n=20
# a=[0]*n
# i,j=0,1
# while i<20:
#   a[i]=j
#   i+=1
#   j+=1
# print(a)

# n=20
# a=[]
# i,j=0,1
# while i<20:
#   a.append(j)
#   i+=1
#   j+=1
# print(a)

'''Q-2.) Write a program to input (n) names from the user and print them.'''
# n=int(input())
# a=[0]*n
# i=0
# while i<n:
#      j=input()
#      a[i]=j
#      i+=1
# print(a)

'''Q-3.) Given an array and its size, print the array in reverse order. (l=[5,4,9,2,1,0])'''
# n=[5,4,9,2,1,0]
# l=len(n)
# new=[]
# i=-1
# while i>=(-l):
#     w=n[i]
#     new+=[w]
#     i-=1
# print(new)

'''With slicing.'''
# n=[5,4,9,2,1,0]
# print(n[::-1])

'''Q-4.) Given a array and its size, print alternate elements from the last.(l=[5,4,9,2,1,0])'''
# l=[5,4,9,2,1,0]
# n=len(l)
# i=-1
# while i>=(-n):
#     if i%2!=0:
#         print(l[i])
#     i-=1

'''Q-5.) Given a list ["a", 1, "2", 5, "b", "q"]. Print the last "i" elements of any given list. "i" accepted from the user.'''
# n=["a", 1, 2, 5, "b", "q"]
# i=int(input())
# l=len(n)
# if i>(-1) and i<l:
#     j=-1
#     while j>=(-i):
#         print(n[j])
#         j-=1
# else:
#     print("Not Valid")

'''Q-6.) Given a list ([1,2,3,4,5,6,7]), take a number from the user and check whether it exists in the list or not.'''
# l=[1,2,3,4,5,"s",6,7]
# n=input()
# if n in l:
#     print("yes")
# else:
#     print("no")

'''Q-7.) Write a program to create a list of n numbers from the user, and print true if the complete list consists of consecutive numbers or not.'''
# n=int(input())
# l=[0]*n
# i,j=0,0
# count=0
# while j<n:
#     a=int(input())
#     l[j]=a
#     j+=1
# while i<(n-1):
#     if (l[i+1]-l[i])==1:
#         count+=1
#     else:
#         print("No")
#         break
#     i+=1
# if count==(n-1):
#     print("Yes")

'''Q-8.) Find the sum and average of elements in a list. Take elements as input from the user.'''
# n=int(input())
# l=[0]*n
# i=0
# sum=0
# while i<n:
#     j=int(input())
#     l[i]=j
#     sum+=l[i]
#     i+=1
# print(sum,",",(sum/n))
# print(l)

'''Q-10.) Write a program to count positive and negative elements in a list. Take elements as input from the user.'''
# n=int(input())
# l=[0]*n
# i=0
# count=0
# count2=0
# while i<n:
#     j=int(input())
#     l[i]=j
#     if l[i]>0:
#         count+=1
#     elif l[i]<0:
#         count2+=1
#     i+=1
# print(l,",","Positive Eelements are",count,",","Negative Elements are",count2)

'''Q-12.) Create a list that stores first n even numbers. Take n as input from the user.'''
# n=int(input())
# l=[0]*n
# i=0
# j=0
# while i<n:
#     if j%2==0:
#         l[i]=j
#         i+=1
#     j+=1
# print(l)

'''Q-13.) Create a list that stores first n odd numbers. Take n as input from the user.'''
# n=int(input())
# l=[0]*n
# i=0
# j=0
# while i<n:
#     if j%2!=0:
#         l[i]=j
#         i+=1
#     j+=1
# print(l)

'''Q-14.) Create a list that stores all the factors of a number n. Take n as input from the user.'''
# n=int(input())
# l=[]
# i=1
# while i<=(n//2):
#   if n%i==0:
#     a=i
#     l.append(a)
#   i+=1
# l.append(n)
# print(l)

'''Q-15.) Create a list that stores all the prime numbers up to n. Take n as input from the user.'''
# n=int(input())
# l=[0]*n
# j=1
# count=1
# a=0
# while count<=n:
#     i,scount=1,0
#     while i<=(j//2):
#         if j%i==0:
#             scount+=1
#         i+=1
#     if scount==1:
#         count+=1
#         l[a]=j
#         a+=1
#     j+=1
# print(l)

'''Q-16.) Create a list that stores perfect numbers up to n. Take n as input from the user.'''
# n=int(input())
# l=[]
# i=1
# while i<=n:
#     j=1
#     sum=0
#     while j<=(i//2):
#         if i%j==0:
#             sum+=j
#         j+=1
#     if sum==i:
#         l.append(i)
#     i+=1
# print(l)

'''Q-17.) Create a list that stores Armstrong numbers up to n. Take n as input from the user.'''
# n=int(input())
# l=[]
# i=1
# while i<=n:
#     m=len(str(i))
#     x=i
#     sum=0
#     while x>0:
#         a=x%10
#         c=a**m
#         sum+=c
#         x=x//10
#     if sum==i:
#         l.append(i)
#     i+=1
# print(l)

'''Q-18.) Create a list that stores the factorial of first n natural numbers. Take n as input from the user.'''
# n=int(input())
# l=[0]*n
# i=1
# x=0
# while i<=n:
#     j=1
#     p=1
#     while j<=i:
#         p*=j
#         j+=1
#     l[x]=p
#     x+=1
#     i+=1
# print(l)

'''Q-19.) Write a program to create a list of n numbers from the user, and count the number of odd and even numbers.'''
# n=int(input())
# l=[0]*n
# i=0
# count=0
# count2=0
# while i<n:
#     j=int(input())
#     l[i]=j
#     if j%2==0:
#         count+=1
#     else:
#         count2+=1
#     i+=1
# print(l)
# print("Even numbers =",count,",","Odd numbers =",count2)

'''Q-20.) Write a program to create a list of n numbers from the user, and sum the elements on odd positions as odds and on even positions as evens.'''
# n=int(input())
# l=[0]*n
# i=0
# sum=0
# sum1=0
# while i<n:
#     a=int(input())
#     l[i]=a
#     if i%2==0:
#         sum+=a
#     else:
#         sum1+=a
#     i+=1
# print(l)
# print("Even position's sum =",sum,"Odd position's sum =",sum1)

'''Q-21.) Construct a flowchart to create a list of n items where n is input from the user. Then input n names from the user and add them to the list.'''
# n=int(input())
# a=[0]*n
# i=0
# while i<n:
#      j=input()
#      a[i]=j
#      i+=1
# print(a)

'''Q-22.) In the flowchart of the above question, print the names input by the user in reverse order.'''
# n=['uma', 'shivani', 'prachi', 'bhawna', 'chandni']
# l=len(n)
# new=[0]*l
# i=-1
# j=0
# while i>=(-l):
#     new[j]=n[i]
#     j+=1
#     i-=1
# print(new)

'''Q-23.) Construct a flowchart to input n numbers from the user. Store them in a list, Then show how to determine the maximum number.'''
# n=int(input())
# a=[0]*n
# i=0
# max=0
# while i<n:
#      j=int(input())
#      if max<j:
#          max=j
#      else:
#         max=max
#      a[i]=j
#      i+=1
# print(a)
# print("max =",max)

'''Q-24.) Construct a flowchart to show how to store the first (n) natural numbers in an array and then show them in the reverse sequence.'''
# n=int(input())
# a=[0]*n
# new=[0]*n
# i,x=0,-1
# j,y=1,0
# while i<n:
#      a[i]=j
#      j+=1
#      i+=1
# print(a)
# while x>=(-n):
#     new[y]=a[x]
#     y+=1
#     x-=1
# print(new)

'''Q-25.) Fibonacci Number.'''
# n=int(input())
# a=0
# i,k=1,1
# print(a,end=',')
# print(i,end=',')
# print(k,end=',')
# while a<(n-3):
#     c=i+k
#     print(c,end=',')
#     k=i
#     i=c
#     a+=1