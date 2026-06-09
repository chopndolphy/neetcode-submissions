import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lookup: List[int] = [None] * len(nums)
        output: List[int] = [None] * len(nums) 

        for i in range(len(nums)): 
            prev = 1 if i == 0 else lookup[i-1]
            lookup[i] = prev * nums[i]
        
        reverse_prod = 1 
        for i in reversed(range(len(nums))):
            prev = 1 if i == 0 else lookup[i-1]
            output[i] = prev * reverse_prod
            reverse_prod *= nums[i]

        
        return output

