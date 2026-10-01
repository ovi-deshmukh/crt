'''
What is sliding window: It is a very important Optimization technique in DSA
Mainly used in :
-->Arrays
--> Lists
-->Strings
-->Purpose: To reduce the time complexity from O(n **2) to O(n)
What:
1) Sub-Arrays 
2) Sub-Strings

Real-World Example:
Ex:   H1 H2 H3 H4 H5
Bus-->Start-->H1 H2 H3
2) H2 H3 H4
3) H3 H4 H5

Types of Sliding Window:
2 types
1) Fixed Sliding 
2) Variable Sliding

1) Fixed Sliding: 
Size of the window is Fixed. Not Change


# Maximum sum of consecutive Sub-array of fixed size k
#Traditional Approach
def max_sum(arr,k):         #arr=[1,2,3,4,5],3
    n =len(arr)         #n=5
    maxsum=0
    for i in range(n-k+1):      #i=(5-3+1)=(2+1)=3-->[0,1,2]
        add = 0
        for j in range(k):
            add = add + arr[i+j]
        maxsum=max(maxsum,add)
    return maxsum
print(max_sum([1,2,3,4,5],3))

#Optimal Solution:
def max_sum2(arr,k):
    maxsum2=0
    add2=sum(arr[:k])
    for i in range(k,len(arr)):  #i=3
        add2 = add2 - arr[i-k] + arr[i]
        maxsum2= max(maxsum2, add2) 
    return maxsum2
print(max_sum([1,2,3,4,5],3))   
'''
#Average of evrey window of size k
def max_sum2(arr,k):
    add2=sum(arr[:k])
    print(add2 / k)

    for i in range(k,len(arr)):  #i=3
        add2 = add2 - arr[i-k] + arr[i]   #9
        print(add2 / k)   
max_sum2([1,2,3,4,5],3)            

#Maximum sub-array sum Window (Return Window)
# arr=[1,2,3,4,5],k=3
# [1,2,3]=6
# [2,3,4]=9
# [3,4,5]=12
# Output-->[3,4,5]

#leetcode: 643, 2269