class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Time Complexity: O(n)
        # Memory Complexity: O(1)
        
        l, total = 0, 0
        res = float("inf")
        
        for r in range(len(nums)):
            
            total += nums[r]
            
            while total >= target: # This will not result in O(N^2) because target will always be a positive number, and                                        loop will exit itself anyway
                
                res = min(r-l +1, res)
                total -= nums[l]
                l += 1
        
        
        
        return 0 if res == float("inf") else res
        