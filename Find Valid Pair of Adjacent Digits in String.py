class Solution:
    def findValidPair(self, s: str) -> str:
        count=Counter(s)
        ans=[]

        l=0
        r=1

        while r<len(s):
            if s[l]!=s[r] and count[s[l]]==int(s[l]) and count[s[r]]==int(s[r]):
                ans.append(s[l])
                ans.append(s[r])
                break
            r+=1
            l+=1

        if ans:
            return "".join(ans)
        else:
            return ""
