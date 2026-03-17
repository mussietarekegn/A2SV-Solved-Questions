class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(numRows-1):
            next_row=[0]*(len(res)+1)
            for j in range(len(res)):
                next_row[j]+=res[-1][j]
                next_row[j+1]+=res[-1][j]
            res.append(next_row)
        return res