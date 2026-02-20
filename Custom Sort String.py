class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=Counter(s)

        res=[]
        
        for ch in order:
            if ch in count:
                res.append(ch*count[ch])
                del count[ch]
        
        for k,v in count.items():
            res.append(k*v)

        return "".join(res)
