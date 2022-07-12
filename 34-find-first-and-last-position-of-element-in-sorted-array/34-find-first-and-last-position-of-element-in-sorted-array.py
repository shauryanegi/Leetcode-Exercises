class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Time Complexity: O(logn) -> Binary Search
        
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
        
    
    def binSearch(self, nums, target, leftBias):
        
        l , r = 0, len(nums) -1
        i = -1
        
        while l <=r:
            
            m = l + ((r - l) // 2) # (l + r) // 2 can lead to overflow
            
            if target > nums[m]:
                l = m + 1
                
            elif target < nums[m]:
                r = m - 1
                
            else:
                i = m
            
                if leftBias:
                    r = m - 1

                else:
                    l = m + 1
                
        return i

            
            
                
        