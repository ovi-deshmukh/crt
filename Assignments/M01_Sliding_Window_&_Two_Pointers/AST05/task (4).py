from typing import List
def productExceptSelf(nums):
    result = [1] * len(nums)

    # Store the product of all values to the left of each index.
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    # Multiply by the product of all values to the right.
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(productExceptSelf(arr))
