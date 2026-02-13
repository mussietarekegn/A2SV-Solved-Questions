class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d=defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])
        
        res=[]
        m=len(mat)
        n=len(mat[0])

        for di in range(m+n-1):
            if di%2==0:
                res.extend(d[di][::-1])
            else:
                res.extend(d[di])
        
        return res
