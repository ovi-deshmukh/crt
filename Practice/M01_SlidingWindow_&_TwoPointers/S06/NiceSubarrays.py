'''
Nice Sub-array:
It is continuous elem of atmost of K element

'''
#Leetcode : 1248
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def most(k):   #divide array into sub-array with atmost of k odd elem
            if k < 0:
                return 0
            left, right =0, 0
            odd =0 
            count = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -=1
                    left += 1
                count += right -left +1
            return count
        return most(k) - most(k-1)
        
#Leetcode : 1763
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        chars= set(s)     #{"Y",'a','z','A','y'}
        for i , c in enumerate(s):     #Returns both index and value
            if c.lower() in chars and c.upper() in chars:
                continue
            left = self.longestNiceSubstring(s[:i])     #self-->Object
            right = self.longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right
        return s
        