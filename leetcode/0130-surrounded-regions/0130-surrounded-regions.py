class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row=len(board)
        col=len(board[0])

        def check(r,c):
            if r>=row or r<0 or c<0 or c>=col or board[r][c]!="O":
                return
            
            board[r][c]="M"
            check(r+1,c)
            check(r-1,c)
            check(r,c+1)
            check(r,c-1)
        
        
        for i in range(row):
            check(i,0)
            check(i,col-1)
        
        for i in range(col):
            check(0,i)
            check(row-1,i)
        
        for i in range(row):
            for j in range(col):

                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="M":
                    board[i][j]="O"
        
                

        
