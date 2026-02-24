class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        
        total=sum(nums)
        n=len(nums)//2
        t=total//n
        res=0

        while l<r:
            if nums[l]+nums[r]!=t:
                return -1
            res+=nums[l]*nums[r]
            r-=1
            l+=1
        
        return res
        
