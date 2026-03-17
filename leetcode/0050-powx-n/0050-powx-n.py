class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1
        if n<0:
            n=abs(n)
            x=1/x
        if n>0:
            res=1
            while n>0:
                if n%2!=0:
                    res=res*x
                n=n//2
                x=x*x
            return res
            

