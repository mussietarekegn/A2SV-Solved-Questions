class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row=len(matrix)
        col=len(matrix[0])
        
        l=0
        r=row-1

        while l<=r:
            mid=(l+r)//2
            
            if matrix[mid][0]==target:
                return True
            if matrix[mid][0]>target:
                r=mid-1
            else:
                ll=0
                rr=col-1

                while ll<=rr:
                    midd=(ll+rr)//2
                    if matrix[mid][midd]==target:
                        return True
                    if matrix[mid][midd]>target:
                        rr=midd-1
                    else:
                        ll=midd+1

                l=mid+1
        
        return False
            