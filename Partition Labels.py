class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i,c in enumerate(s):
            last_index[c]=i
        size,end=0,0
        r=[]
        for i,c in enumerate(s):
            size+=1
            end=max(end,last_index[c])
            if i==end:
                r.append(size)
                size=0
        return r
