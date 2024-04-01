import numpy as num
# array1=num.array([2,4,5,6,7,7])
# print(f"1D={array1[2]}")
# array2=num.array([[2,3,4,5,6,],[6,5,5,6,66,]])
# print(f"1D={array2[1][4]}")
# array3=num.array([[[2,3,4,6,5,6],[9,5,7,8,1,11]],[[12,90,5,43,54,78],[12,32,75,5,67,87]]])
# print(f"1D={array3[1][0][4]}")
# i=0
# while i<len(array3):
#     j=0
#     while j<len(array3[0]):
#         l=0
#         while l<len(array3[0][0]):
#             # print(array3[i][j][l])
#             if (array3[i][j][l])==5:
#                 array3[i][j][l]=5000
#             l+=1
#         j+=1     
#     i+=1    
# # print(*array3)
# if 3 in array1:
#     print("yes")
# else:
#     print("NO")

# if 3 in array2:
#     print("yes")
# else:
#     print("NO")    

# if 3 in array3:
#     print("yes")
# else:
#     print("NO")


'''1) insert'''
'''2) append'''

array1=num.array([2,4,5,6,7,7])
# array1=num.insert(array1,2,2000)
# print(array1)

'''1) remove'''
'''2) pop'''
'''3) delete'''
'''4) shift'''
array1.remove(2)
print(array1)
