class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]

        for i in range(len(matrix[0])):
            tem=[]
            for j in range(len(matrix)):
                tem.append(matrix[j][i])
            ans.append(tem)
        
        return ans
