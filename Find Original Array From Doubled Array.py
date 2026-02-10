class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count=Counter(changed)
        ans=[]

        for num in changed:
            if num==0:
                continue
            if num in count and num*2 in count:
                ans.append(num)
                count[num]-=1
                count[num*2]-=1
            if count[num]==0:
                del count[num]
            if count[num*2]==0:
                del count[num*2]
        
        if count[0]%2==0:
            n=count[0]//2
            for i in range(n):
                ans.append(0)
        
        if len(ans)==len(changed)/2:
            return ans
        else:
            return []
