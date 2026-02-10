class Solution:
    def isHappy(self, n: int) -> bool:
        ans=set()
        num=n

        while n!=1:
            summ=0
            while num>0:
                dig=num%10
                num=num//10
                summ+=dig*dig
            num=summ
            if num in ans:
                break
            else:
                ans.add(num)
        
        if num==1:
            return True
        else:
            return False


        

        

        
