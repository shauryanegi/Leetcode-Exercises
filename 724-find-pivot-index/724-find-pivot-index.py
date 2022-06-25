class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum = sum(nums) #O(n) operation

        leftSum = 0

        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum

            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]

        return -1