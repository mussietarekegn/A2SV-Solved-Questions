class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        di = [[0,1],[1,0],[0,-1],[-1,0]]
        res = []
        r, c = rStart, cStart
        
        res.append([r, c])  # add starting position
        
        steps = 1
        i = 0
        
        while len(res) < rows * cols:
            
            for x in range(2):
                dr, dc = di[i]   
                for y in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                
                i = (i + 1) % 4 
            
            steps += 1
        
        return res
