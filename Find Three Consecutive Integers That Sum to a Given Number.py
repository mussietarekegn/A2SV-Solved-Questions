class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans=[]
        if num%3==0:
            a=num//3
            ans.append(a-1)
            ans.append(a)
            ans.append(a+1)
        return ans
