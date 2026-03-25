class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        
        def helper(start,combo):
            if len(combo)==k:
                ans.append(combo[:])
                return 
            
            for nc in range(start,n+1):
                combo.append(nc)
                helper(nc+1,combo)
                combo.pop()
        
        helper(1,[])

        return ans