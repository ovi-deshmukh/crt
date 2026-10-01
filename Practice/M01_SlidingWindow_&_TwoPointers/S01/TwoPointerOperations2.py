'''Write a python code to remove odd numbers from the array?
Ex: arr=[10, 20, 45, 78, 12]
O/P: [10, 20, 78, 12] 

#Brute Solution:
def remove1(arr):
    res=[]
    for num in arr:
        if num % 2 ==0: #10/2==0:
            res.append(num)
    return res
arr=[10, 20, 45, 78, 12,55,75,89]
print(remove1(arr))

#Optimized Solution:
arr=[10, 20, 45, 78, 12,55,75,89]
arr.sort()
slow = 0
for fast in range(len(arr)):    
    if arr[fast] % 2 ==0:      
        arr[slow]=arr[fast] 
        slow +=1
print(arr[:slow])

Leetcode: 
1) 26
2) 27
3) 167
4) 283
5) 977

'''