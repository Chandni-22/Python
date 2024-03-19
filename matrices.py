'''Q-1.) Creating a Matrices.'''
# n=int(input())
# m=int(input())
# a=[0]*n
# i=0
# while i<n:
#     a1=[0]*m
#     j=0
#     while j<m:
#         l=int(input())
#         a1[j]=l
#         j+=1
#     a[i]=a1
#     i+=1
# print(a)

'''Q-2.) Write a Python Program to add two matrices and store them in a separate matrix.'''
# A=[[2, 4, 1],
#    [8, 0, -1],
#    [7, -3, 0]]
# B=[[8, 0, 3],
#    [2, -5, 7],
#    [3, -1, 5]]
# l=len(A)
# i=0
# C=[0]*l
# while i<l:
#     j=0
#     C1=[0]*l
#     while j<l:
#         s=(A[i][j])+(B[i][j])
#         C1[j]=s
#         j+=1
#     C[i]=C1
#     i+=1
# print(C)

'''Q-3.) Write a program to subtract two matrices and store them in a separate matrix.'''
# A=[[2, 4, 1],
#    [8, 0, -1],
#    [7, -3, 0]]
# B=[[8, 0, 3],
#    [2, -5, 7],
#    [3, -1, 5]]
# l=len(A)
# i=0
# C=[0]*l
# while i<l:
#     j=0
#     C1=[0]*l
#     while j<l:
#         s=(A[i][j])-(B[i][j])
#         C1[j]=s
#         j+=1
#     C[i]=C1
#     i+=1
# print(C)

'''Q-4.) Write a program to multiply two matrices and store the result in a separate matrix.'''
# A=[[2, 4, 1],
#    [8, 0, -1],
#    [7, -3, 0]]
# B=[[8, 0, 3],
#    [2, -5, 7],
#    [3, -1, 5]]
# i=0
# l=len(A)
# C=[0]*l
# while i<l:
#     j=0
#     C1=[0]*l
#     while j<l:
#         sum=0
#         z=0
#         while z<l:
#             p=(A[i][z])*(B[z][j])
#             sum+=p
#             z+=1
#         C1[j]=sum
#         j+=1
#     C[i]=C1
#     i+=1
# print(C)

'''Q-5.) Write a Python program to transpose matrix A. Store the result in a separate matrix.'''
# A=[[2, 4, 1],
#   [8, 0, -1],
#   [7, -3, 0]]
# l=len(A)
# B=[0]*l
# i=0
# while i<l:
#     j=0
#     ln=len(A[i])
#     B1=[0]*ln
#     while j<ln:
#         B1[j]=A[j][i]
#         j+=1
#     B[i]=B1
#     i+=1
# print(B)

'''Q-6.) Write a program that rotates the elements of a list so that the elements at the first index moves to the second and element at the second index move to the third and so on. The last element moves at the first index.'''
# A=[[2, 4, 1],
#    [8, 0, -1],
#    [7, -3, 0]]
# l=len(A)
# i=0
# C=[0]*l
# while i<l:
#     j=0
#     m=len(A[i])
#     C1=[0]*m
#     while j<(m):
#         C1[j]=A[i][j-1]
#         j+=1
#     C[i]=C1
#     i+=1
# print(C)

'''Q-7.) Write a Program to check whether a given matrix is an identity matrix or not. Identity matrix: Each main diagonal element is equal to 1, and the remaining elements of the matrix are equal to 0.'''
# A=[[1,0,0],
#    [0,1,0],
#    [0,0,1]]
# c=0
# i=0
# l=len(A)
# k=len(A[i])
# if l==k:
#     while i<l:
#         j=0
#         while j<k:
#             if i==j and A[i][j]==1:
#                 c+=1
#             elif A[i][j]==0 and i!=j:
#                 c+=1
#             else:
#                 i=l
#                 break
#                 print("Not an Identity Matrices")
#             j+=1
#         i+=1
# if c==(l*l):
#     print("Identity Matrices")
# else:
#     print("Not a Identity Matrices")

'''Q-8.) Write a Program to find whether the given matrix is diagonal or not.'''
# A=[[1,0,1],
#    [0,2,0],
#   [0,0,1]]
# c=0
# i=0
# l=len(A)
# k=len(A[i])
# if l==k:
#     while i<l:
#         j=0
#         while j<k:
#             if i==j:
#                 c+=1
#             elif i!=j and A[i][j]==0:
#                 c+=1
#             else:
#                 i=l
#                 break
#                 print("Not an Diagnol Matrices")
#             j+=1
#         i+=1
# if c==(l*l):
#     print("Diagonal Matrices")
# else:
#     print("Not an Diagonal Matrices")

'''Q-9.) Write a Program to find the sum of all diagonal elements of a matrix.'''
# A=[[5,0,0],
#    [0,2,0],
#    [0,0,5]]
# i=0
# j=0
# sum=0
# l=len(A)
# while i<l:
#     sum+=A[i][j]
#     i+=1
#     j+=1
# print(sum)

'''Q-10.) Write a Program to find the maximum element in the matrix.'''
# A=[[2, 4, 1],
#    [8, 0, -1],
#    [7, -3, 0]]
# i=0
# max=0
# l=len(A)
# while i<l:
#     j=0
#     while j<l:
#         p=A[i][j]
#         if max<p:
#             max=p
#         else:
#             max=max
#         j+=1
#     i+=1
# print(max)

'''Q-11.) Write a Program to find the minimum element in the matrix.'''
# A=[[2, -1, 1],
#    [8, -10, -5],
#    [7, 1, 0]]
# i=0
# min=0
# l=len(A)
# while i<l:
#     j=0
#     while j<l:
#         p=A[i][j]
#         if min>p:
#             min=p
#         else:
#             min=min
#         j+=1
#     i+=1
# print(min)

'''Q-12.) Write a Program to find the position of an element in a 2d array or Matrix.'''
# n=int(input())
# A=[[2, -1, 1],
#    [8, -10, -5],
#    [7, 1, 0]]
# i=0
# a=0
# l=len(A)
# while i<l:
#     j=0
#     while j<l:
#         if A[i][j]==n:
#             print(i,",",j)
#             i+=l
#             a+=1
#             break
#         else:
#             j+=1
#     i+=1
# if a==0:
#     print("-1")