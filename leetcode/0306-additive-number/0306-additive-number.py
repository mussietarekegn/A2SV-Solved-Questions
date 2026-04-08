class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)

        def helper(n1,n2,r):
            while r:
                s=str(int(n1)+int(n2))
                if not r.startswith(s):
                    return False
                r=r[len(s):]
                n1,n2=n2,s
            return True

        for i in range(1,n):
            for j in range(i+1,n):
                num1=num[:i]
                num2=num[i:j]
                if ((len(num1)>1 and num1[0]=='0') or (len(num2)>1 and num2[0]=='0')):
                    continue
                if helper(num1,num2,num[j:]):
                    return True
        return False

        
            