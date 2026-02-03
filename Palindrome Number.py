class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        dig=0
        num=x
        while num>0:
            dig+=num%10
            num//=10
            dig*=10
        
        dig//=10
        
        if dig==x:
            return True
        else:
            return False
