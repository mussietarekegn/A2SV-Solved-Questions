class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=4

        while n>0:
            if mat==target:
                return True

            for i in range(len(mat)):
                for j in range(i+1,len(mat)):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            
            for i in range(len(mat)):
                mat[i].reverse()
            
            n-=1
        
        return False
            
            
