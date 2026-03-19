class Solution:
    def lastRemaining(self, n: int) -> int:
        s=1
        step=1
        many=n
        l=True

        while many>1:
            if l or many%2==1:
                s+=step
            many//=2
            step*=2
            l=not l
        
        return s
        
    