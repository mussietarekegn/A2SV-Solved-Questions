class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def helper(x,n):
            res=1
            while n>0:
                if n%2!=0:
                    res=(res*x)%(10**9+7)
                n=n//2
                x=(x*x)%(10**9+7)
            return res
        
        e=ceil(n/2)
        p=n//2

        return (helper(5,e)*helper(4,p))%(10**9+7)