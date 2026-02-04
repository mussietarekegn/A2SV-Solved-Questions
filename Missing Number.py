class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        interval=0
        # l=0
        # r=1

        # while r<len(nums):
        #     interval=nums[r]-nums[l]
        #     if interval>1:
        #         return nums[l]+1
        #     l+=1
        #     r+=1

        # if nums[0]!=0:
        #     return 0

        # return len(nums)

        for i in range(len(nums)):
            if i!=nums[i]:
                return i
                
        return len(nums)
