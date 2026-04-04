class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pd=set()
        nd=set()
        arr=[["."]*n for i in range(n)]
        res=[]

        def helper(r):
            if r==n:
                copy=["".join(row) for row in arr]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r+c) in pd or (r-c) in nd:
                    continue
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                arr[r][c]="Q"

                helper(r+1)

                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                arr[r][c]="."
        
        helper(0)
        return res