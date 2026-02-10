class Solution:
    def romanToInt(self, s: str) -> int:
        mapp={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans=0

        for i in range(len(s)):
            if i+1<len(s) and mapp[s[i]]<mapp[s[i+1]]:
                ans-=mapp[s[i]]
            else:
                ans+=mapp[s[i]]
        
        return ans
        
        return ans
            
