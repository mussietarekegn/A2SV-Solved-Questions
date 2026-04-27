class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(arr)):
            min_idx = i

            for j in range(i+1,len(arr)):
                if arr[j] <= arr[min_idx]:
                    min_idx = j
            
            arr[i],arr[min_idx] = arr[min_idx],arr[i]