class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Time Complexity: O(n)
        # Memory Complexity: O(1)
        
        l,r = 0,1
        maxP = 0
        
        while r < len(prices):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                
            else:
                l = r # In cases where r is very low, we would want the l to go there and replace the lowest position
                
            r += 1
            
        return maxP
                
        