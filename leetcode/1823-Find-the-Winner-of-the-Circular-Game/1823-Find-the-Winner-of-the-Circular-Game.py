class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(nums,k,ind):
            if len(nums)==1:
                return nums[0]
            i=(k-1+ind)%len(nums)
            nums.pop(i)
            return helper(nums,k,i)
        
        nums=[]
        for i in range(n):
            nums.append(i+1)
        
        return helper(nums,k,0)