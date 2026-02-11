class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count=Counter()
        
        for res in responses:
            val=set(res)
            for ele in val:
                count[ele]+=1
        
        maxx=max(count.values())
        ans=[]

        for k,v in count.items():
            if v==maxx:
                ans.append(k)
        
        return min(ans)
