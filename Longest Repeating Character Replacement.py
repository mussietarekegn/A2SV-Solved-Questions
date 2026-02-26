class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        l=0
        max_len=0
        max_=0

        for r in range(len(s)):
            count[s[r]]+=1
            max_=max(max_,count[s[r]])
            while (r-l+1)-max_>k:
                count[s[l]]-=1
                if count[s[l]]==0:
                    count.pop(s[l])
                l+=1
            max_len=max(max_len,r-l+1)
        
        return max_len
