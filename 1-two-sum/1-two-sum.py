class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time Complexity: O(n)
        # Memory Complexity: O(n) -> adding a hashmap
        
        prevMap = {}
        
        for index, number in enumerate(nums):
            diff = target - number
            
            if diff in prevMap:
                return [prevMap[diff], index]
            
            prevMap[number] = index
            
            
            
        