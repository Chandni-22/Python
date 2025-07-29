'''Have to change'''
# n=int(input())
# A=[1,2,3,4,5,7,8,16,19]
# a=A
# count=0
# while count<1:
#     lent=len(a)
#     if lent%2==0:
#         left=(lent//2)-1
#         right=(lent//2)
#         if a[left]<n:
#             if a[right]<n:
#                 a=a[right:]
#             elif a[right]>n:
#                 break
#             else:
#                 count+=1    
#         elif a[left]>n:
#             a=a[:left+1]
#         else:
#             count+=1       
#     else:
#         left=(lent//2)-1
#         mid=(lent//2)
#         right= (lent//2)+1  
#         if mid>n:
#             if a[left]<n:
#                 break
#             elif a[left]>n:
#                 a=a[:left+1]
#             else:
#                 count+=1 
#         elif mid<n:
#             if a[right]<n:
#                 a=a[right:]
#             elif a[right]>n:
#                 break
#             else:
#                 count+=1
#         else:
#             count+=1 
# if count==1:
#     print("YES")        
# else:
#     print("NO")

'''Correct'''
# a=[1,2,3,4,5,7,8,16,19]
# n=16
# end=len(a)-1
# start=0
# while start<=end:
#     mid=start+((end-start)//2)
#     if a[mid]<n:
#         start=mid+1
#     elif a[mid]>n:
#         start=mid-1
#     else:
#         print(mid)
#         break