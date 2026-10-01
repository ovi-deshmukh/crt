'''
Binary ->0's & 1's
Ex: [1,0,1,0]
[1]
[1,0]
[1,0,1]
[1,0,1,0]
[0]
[0,1]
-------
-------
[1,1]-->Not a sub-array (Sub-Sequence)

'''
'''
#Leetcode : 1493
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right =0, 0
        ans = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans +=1 
            while ans > 1:
                if nums[left] == 0:
                    ans -=1
                left +=1
            max_len=max(max_len , right-left+1)
        return max_len -1

#Leetcode : 1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right =0,0
        ans =0
        max_len =0
        for right in range(len(nums)):
            if nums[right] == 0:
                ans +=1
            while ans > k:
                if nums[left] == 0:
                    ans -=1
                left += 1
            max_len = max(max_len,right-left +1)
        return max_len

#Leetcode : 930
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def most(k):  #want to divide into sub-array with sum atmost K
            if k < 0:
                return 0
            left,right =0, 0
            cur_sum =0
            count =0
            for right in range(len(nums)):
                cur_sum += nums[right]
                while cur_sum > k:
                    cur_sum -= nums[left]
                    left +=1
                count += right -left +1
            return count
        return most(goal) - most(goal-1)
'''