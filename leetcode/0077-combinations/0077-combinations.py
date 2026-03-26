class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        
        def helper(start,combo):
            if len(combo)==k:
                ans.append(combo[:])
                return 
            if start>n:
                return 
            combo.append(start)
            helper(start+1,combo)
            combo.pop()
            helper(start+1,combo)
        
        helper(1,[])

        return ans