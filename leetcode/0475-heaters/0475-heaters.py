class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res=0
        for hoe in houses:
            pos=bisect.bisect_left(heaters,hoe)
            if pos==0:
                left=float('inf')
            else:
                left=abs(hoe-heaters[pos-1])
            if pos==len(heaters):
                right=float('inf')
            else:
                right=abs(heaters[pos]-hoe)
            dis=min(right,left)
            res=max(res,dis)
        return res