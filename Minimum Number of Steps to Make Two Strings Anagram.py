class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=Counter(s)
        n=0
        for i in range(len(t)):
            if t[i] not in count:
                n+=1
            if t[i] in count:
                count[t[i]]-=1
            if count[t[i]]==0:
                del count[t[i]]
        
        return n
