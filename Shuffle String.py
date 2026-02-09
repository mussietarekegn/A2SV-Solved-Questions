class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapp=defaultdict(int)
        for i in range(len(indices)):
            mapp[indices[i]]=s[i]
        
        ans=[0]*len(s)

        for i in range(len(s)):
            ans[i]=mapp[i]
        
        return "".join(ans)
