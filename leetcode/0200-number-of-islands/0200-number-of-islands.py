class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num=0
        row=len(grid)
        col=len(grid[0])

        def count(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]=="0":
                return 
            
            grid[r][c]="0"
    
            count(r,c-1)
            count(r,c+1)
            count(r-1,c)
            count(r+1,c)

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    num+=1
                    count(i,j)
        
        return num