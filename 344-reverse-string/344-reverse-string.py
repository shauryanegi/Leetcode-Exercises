class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Time O(n), Memory O(1) -> Since operating in the same array
        
        l,r = 0, len(s)-1
        
        while l<r:
            s[l],s[r] = s[r], s[l]
            l = l+1
            r = r-1
            