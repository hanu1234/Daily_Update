# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent
# elements if they are in wrong order.
# In the worst case scenario we need to swap all the elements
# time complexity is O(n2)


def bubble_sort(nums):
    n = len(nums)
    for j in range(n-1):
        for i in range(n - j - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    print(nums)


bubble_sort([5, 3, 6, 2, 1])


# l1 = [5,2,6,2,1]
'''
len = 5
j= 0 to 4 
-->j = 0
-----> i = 0 to 5 - j -1

first iteration:
j = 0 
  ---> i=0 to 4
       i = 0
       i = 1
       i = 2
       i = 3
j =1
   ---> i = 0 to 3
        i = 0
        i = 1
        i = 2
        
'''