class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]

        for el in range(len(arr),1,-1):

            index=0
            for i in range(el):
                if arr[i]==el:
                    index=i
                    break
            
            if index==el-1:
                continue
            
            if index!=0:
                res.append(index+1)
                arr[:index+1]=arr[:index+1][::-1]
            
            res.append(el)
            arr[:el]=arr[:el][::-1]
        
        return res
