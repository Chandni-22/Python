# 1.)Search Insert Position
'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
# nums=list(map(int,input().split()))
# target=int(input())

# if target in nums:
#     print(nums.index(target))
# else:
#     count=0
#     i=0
#     while i<(len(nums)):
#         if target<nums[i]:
#             a=i
#             count+=1
#             break
#         i+=1
#     if count>0:
#         print(a)
#     else:
#         print(len(nums)) 