class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        res=[[0]*col for _ in range(row)]

        for i in range(row):
            k=0
            for j in range(col-1,-1,-1):
                res[i][k]=image[i][j]
                k+=1

        for i in range(row):
            for j in range(col):
                if res[i][j]==0:
                    res[i][j]=1
                else:
                    res[i][j]=0
        
        return res
