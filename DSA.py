'''Data Structures & Algorithm is a particular way of storing and organizing data step by step logically in a computer so that it can be used efficiently.'''

# 1.  Big O / Time Complexity
# 2.  Array
# 3.  List
# 4.  Dictionary
# 5.  Tuple
# 6.  Oops
# 7.  Linked list(sinkly and doubly)
# 8.  Stack
# 9.  Recursion
# 10. Tree.binary tree
# 11. sorting
# 12. binary heap
# 13. graph alogorithem
# 14. backtracking

'''Sorting'''

'''1. sorted(): A built-in method.'''
# List=[9,5,1,3,2,4,7,8,6]
# List.sort()
# print(List)

'''2. Bubble Sort: Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements left to right if they are in the wrong order.'''
# List=[9,7,1,6,2,4,5,8,3]
# l=len(List)
# i=0
# while i<l:
#     j=0
    # while j<(((l)-i)-1):
#         if List[j]>List[j+1]:
#             List[j],List[j+1]=List[j+1],List[j]
#         j+=1
#     i+=1    
# print(List)

'''3. Insertion Sort: Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration. Insertion sort works similarly as we sort cards in our hand in a card game. We assume that the first card is already sorted then, we select an unsorted card.'''
# List=[9,7,1,6,2,4,5,8,3]
# l=len(List)
# i=1
# while i<l:
#     key=List[i]
#     j=i-1
#     while (j>=0) and (key<List[j]):
#         List[j+1]=List[j]
#         j-=1
#     List[j+1]=key
#     i+=1
# print(List)

'''4. Merge Sort: Merge sort continuously cuts down a list in half until each has only one item, then merges those sublists into a sorted list.'''
# def mergeSort(List):
#     if len(List)>1:
#         cent=(len(List))//2
#         left=List[:cent]
#         right=List[cent:]

#         print(f"Left:{left}, Right:{right}")
#         mergeSort(left)
#         mergeSort(right)

#         i,j,k=0,0,0
#         while (i<len(left)) and (j<len(right)):
#             if left[i]<=right[j]:
#                 List[k]=left[i]
#                 i+=1
#             else:
#                 List[k]=right[j]
#                 j+=1
#             k+=1

#         while i<len(left):
#             List[k]=left[i]
#             i+=1
#             k+=1

#         while j<len(right):
#             List[k]=right[j]
#             j+=1
#             k+=1
#         print(List)    

# List=[9,7,6,2,1,4,5,8,3]
# print(f"Sorted list:{mergeSort(List)}")

'''5. Quick Sort: Quick Sort picks a pivot, moves all elements smaller than the pivot to its left, and all elements larger than the pivot to its right. It repeats this process for each partition until the entire array is sorted.'''
# def quickSort(list,left,right):
#     if left<right:
#         pi=partition(list,left,right)

#         quickSort(list,left,(pi-1))
#         quickSort(list,(pi+1),right)   

# def partition(list,left,right):
#     i=left
#     j=right-1
#     pivot=list[right]
#     print(f"Pivot:{pivot}")

#     while i<j:
#         while (i<right) and (list[i]<pivot):
#             i+=1
#             print(f"i:{i}, list[i]:{list[i]}")
#         while (j>left) and (list[j]>=pivot):
#             j-=1
#             print(f"j:{j}, list:{list[j]}")
#         if i<j:
#             list[i],list[j]=list[j],list[i] 
#             print(list) 

#     if list[i]>pivot:
#         list[i],list[right]=list[right],list[i]
#         print(list)   
#     return (i)   

# List=[9,7,6,2,1,4,5,8,3]
# quickSort(List,0,(len(List)-1))
# print(f"Sorted list:{List}")