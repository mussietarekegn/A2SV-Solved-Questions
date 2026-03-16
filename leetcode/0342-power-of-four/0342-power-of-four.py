class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.helper(n,0)
    def helper(self,n,a):
        if 4**a==n:
            return True
        else:
            if 4**a>n:
                return False
        
        return self.helper(n,a+1)
