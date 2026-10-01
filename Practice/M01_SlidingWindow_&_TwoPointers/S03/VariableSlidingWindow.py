'''
Sliding Window:
Types:
1. Fixed --> the size of the window is always fixed
2. Variable 

2. Variable Sliding Window:
--> The size not fixed 
--> size may be increase or decrease based upon the condition
Ex: [2,42,45,8,72,3]
[2]
[2,42]
[2,42,45]
[42,45]
[42,45,8]
-------
-------
-------
Real-World Appli:
Meesho Application-->Products Cart upto to my amount

Algorithm for Variable Sliding:
step-1: We have to use Two -pointers
step-2: for loop(True):
Step-3: Expand my window
Step-4: Check with condition
Step-5: if condition is false:
Step-6: Shrink the window
step-7: Update the answer

How to identify, Which sliding window will be used in the problem solving:

Fixed Size:           Variable:
1. Size K            1. Atmost K
2. Length K          2. Almost K
                     3. Minimum & Maximum

#Find the longest sub-array with sum less than or equal to K
# arr=[2,1,3,2,1] k=6
def longest(arr,k):
    left = 0
    right = 0
    add = 0
    max_len = float('-inf')
    for right in range(len(arr)):
        add += arr[right]
        while add > k:
            add -= arr[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
print(longest([2,1,3,2,1],6))
'''
#Find the smallest sub-array with sum greater than or equal to K
def smallest(arr,k):
    left = 0
    right = 0
    add = 0
    min_len = float('inf')   #min_len= len(arr)+1
    for right in range(len(arr)):
        add += arr[right]
        while add >= k:
            min_len = min(min_len, right-left +1)
            add -= arr[left]
            left += 1
    return 0 if min_len == float('inf') else min_len
print(smallest([2,1,3,2,1],6))

#leet Code: 209 ,713, 904