class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in seen:
                return [seen[second], i]
            else:
                seen[nums[i]] = i