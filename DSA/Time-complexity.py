# What is Time and Space Complexity?
'''
1.)Time complexity: is like how long it takes to cook the dish depending on how much food you're making. If you're cooking for one person, it might take 10 minutes, but if you're cooking for 10 people, it might take much longer. So, time complexity tells you how the cooking time changes as the amount of food (input size) increases.
2.)Space complexity: is like how much kitchen space you need to prepare the dish. If you're making a small meal, you might only need a little counter space, but for a big feast, you might need the entire kitchen. Space complexity tells you how much space (memory) you'll need as the amount of food (input size) grows.
'''

# Why are They Important?
'''
1.)Choose the most efficient algorithm for a given problem.
2.)Predict how an algorithm will scale with larger inputs.
3.)Optimize code for better performance.
'''

# Big O: represents an algorithm's worst-case complexity of 'n', how bad things can get when the input is really big.
'''
1.)Constant time O(1): (Excellent/Best) This means that the run time will always be the same regardless of the input size.
Ex: Calculating the sum of 2 numbers.
YUK-ZKU
2.)Logarithmic time O(log n): (Second best) As the input gets bigger, the time grows slowly by dividing it in half each time.
Ex: Binary search algorithm, which can find a specific value in a sorted list of n items by successively dividing the list into half at each iteration.

3.)Linear time O(n): (Fair) The runtime grows linearly with the input size.
Ex: If it takes 1 minute to do 1 thing, it’ll take 10 minutes for 10 thing.

4.)Log-linear time O(n log n): (Bad) Mix of linear and logrithmic time.
Ex: Shorthing each array in a nested array.

5.)Quadratic time O(n^2): (Worst) as the size of the input gets bigger, the time grows in proportion to the square of the input size (mostly in nested loops).
Ex: Print each items in a nested array.

6.)Exponential time O(2^n): (Worst) 
Ex: 

7.)Factorial time O(n!): (Worst) 
Ex: 
'''


# n=int(input())
# a=[1,2,3,4,5,7,8,16,19]
# count=0
# lent=len(a)
# while count<1:
#     if lent%2==0:
#         left=(lent//2)-1
#         right=(lent//2)
#         if a[left]<n:
#             if a[right]<n:
#                 lent=right+1
#             elif a[right]>n:
#                 break
#             else:
#                 count+=1    
#         elif a[left]>n:
#             lent=left+1
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
#                 lent=left+1
#             else:
#                 count+=1 
#         elif mid<n:
#             if a[right]<n:
#                 lent=right+1
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