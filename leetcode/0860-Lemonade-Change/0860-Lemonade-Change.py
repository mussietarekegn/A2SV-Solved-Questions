class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mapp=defaultdict(int)
        for i in range(len(bills)):
            val=bills[i]
            while bills[i]>5:
                if bills[i]//2 not in mapp:
                    if bills[i]//4 not in mapp or mapp[bills[i]//4]<3:
                        return False
                    mapp[bills[i]//4]-=3
                    if mapp[bills[i]//4]==0:
                        mapp.pop(bills[i]//4)
                    bills[i]//=2
                else:
                    mapp[bills[i]//2]-=1
                    if not mapp[bills[i]//2]:
                        mapp.pop(bills[i]//2)
                bills[i]//=2
            mapp[val]+=1
        return True