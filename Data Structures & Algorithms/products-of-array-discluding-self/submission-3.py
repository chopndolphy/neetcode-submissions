class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = [None] * len(nums) 

        output[0] = 1
        for i in range(1, len(nums), 1):   
            output[i] = output[i-1] * nums[i-1]
        
        postfix = 1 
        for i in reversed(range(len(nums))):
            output[i] *= postfix
            postfix *= nums[i]

        
        return output

