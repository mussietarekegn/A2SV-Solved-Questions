class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s=[str(num) for num in nums]

        for i in range(len(s)):
            for j in range(len(s)-1):
                if s[j]+s[j+1]<s[j+1]+s[j]:
                    s[j],s[j+1]=s[j+1],s[j]
        
        if s[0]=="0":
            return s[0]
        
        return "".join(s)
        
