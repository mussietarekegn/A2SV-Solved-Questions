class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        ranges.sort()

        interval=right-left
        m=0
        if interval>1:
            m=right-1
        lc=0
        rc=0
        intc=0

        merge=[]

        for rang in ranges:
            if not merge or rang[0]>merge[-1][1]+1:
                merge.append(rang)
            else:
                merge[-1][1]=max(merge[-1][1],rang[1])

        for rang in merge:
            if rang[0]<=left and rang[1]>=right:
                lc+=1
            if rang[0]<=right and rang[1]>=right:
                rc+=1
        
        if lc>0 and rc>0:
            return True
        else:
            return False
             

