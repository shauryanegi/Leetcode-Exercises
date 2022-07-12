class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # O(sqrt(n)) solution
        
        # for i in range(1, num+1):
        #     if i * i == num:
        #         return True
        #     if i * i > num:
        #         return False
        
        
        # O(logn) solution
        
        l , r = 1, num
        
        while l <= r:
            mid = l + ((r-l)) // 2  # To avoid the integer overflow problem
            
            if mid * mid > num:
                r = mid - 1
                
            elif mid * mid < num:
                l = mid + 1
                
            else:
                return True
        
        return False
            
            