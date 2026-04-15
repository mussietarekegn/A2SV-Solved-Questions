class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        def back(i):
            if i==len(s):
                res.append(" ".join(curr))
            
            for j in range(i,len(s)):
                w=s[i:j+1]
                if w in wordDict:
                    curr.append(w)
                    back(j+1)
                    curr.pop()
        res=[]
        curr=[]
        back(0)
        return res