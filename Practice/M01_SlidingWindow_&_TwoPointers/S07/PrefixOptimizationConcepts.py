'''
what is Prefix : The array elements from starting of the index to up to the current index 

Ex: a =[1,2,3,4,5]

prefix[0]  = [1]
prefix[1] = [1,2]
prefix[2] = [1,2,3]
prefix[3] = [1,2,3,4]
prefix[4] = [1,2,3,4,5]

Prefix Sum: 
prefix_sum[0]  = 0
prefix_sum[1]  = 1
prefix_sum[2]  = 3
prefix_sum[3]  = 6
prefix_sum[4]  = 10

Res = [0,1,3,6,10]
Formula for prefix_sum :
prefix[i] = prefix[i-1] + nums[i]    (i= 1)

Ex: prefix[1] = prefix[0] + nums[1]

why Prefix is used : 
Suppose, i want to calculate the sum from 2 to 4:
Ex: a =[1,2,3,4,5]
sum(2,4)=[3,4,5]= 3+4+5 = 12

Without prefix : Every time we take the sum of every index ....O(n**2)
With Prefix : First we find the total sum, and we can easily find the values  ...O(1)

Formula: 
sum(L,R) =prefix[R] - prefix[L-1]
(or)
sum(L,R) = prefix[R+1] - prefix[L]

Ex: sum(2,4)=[4]-[3] ==> 10-6 => 4

Ex: [1,7,3,6,5,6]==>3,6,5=3+6+5=14
[0,1,8,11,17,22]
sum(2,4)=[5]-[2]=22-8=14

Diff btw :
    Sliding Window:                                 Prefix Optimization:
1.Positive num in the array                 1. Both +ve and -ve num in the array
2.Window size may be fixed or Extend         2. Need Exact Count 
also it can shrink
'''

#Leet code : 724
#Pivot Index : 
# Sum of all leftmost eleme == Sum of all Rightmost eleme 
'''
nums=[1,7,3,6,5,6]    

Algorithm : 
1) Calculate total sum
2) initial value of left_sum is zero
3) Traverse all the array ele
4) Right_sum = total - left_sum - nums[i]
5) Compare left_sum == Right_sum 
6) return particular index
7) update left_sum
8) return -1
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            Right_sum = Total_sum - Left_sum - nums[i] 
            if Left_sum == Right_sum:
                return i
            Left_sum += nums[i]
        return -1

#Leet code : 1991
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            Right_sum = Total_sum - Left_sum - nums[i] 
            if Left_sum == Right_sum:
                return i
            Left_sum += nums[i]
        return -1
        

#Leet code : 1732
'''
Algorithm : 
1) Curr_alti = 0
2) Iniital value high_alti = 0
3) Traverse your elements
4) Update Curr_alti
5) Calculate the maximum of high_alti
6) return Maxi of high_alti
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alti = 0
        maxi_alti = 0
        for change in gain:
            cur_alti += change
            maxi_alti = max(maxi_alti, cur_alti)
        return maxi_alti
        
#Leet code : 2574