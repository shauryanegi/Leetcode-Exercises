class Solution:
    def mySqrt(self, x: int) -> int:
        
        l , r = 0, x
        
        while l <= r:
            
            mid = l + ((r-l)) // 2  # To avoid the integer overflow problem
            
            if mid * mid > x:
                r = mid - 1
                
            elif mid * mid < x                            :
                l = mid + 1
                
            else:
                return mid
            
        return r
    
    