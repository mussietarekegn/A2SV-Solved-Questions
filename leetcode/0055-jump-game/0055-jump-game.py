class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # if nums[0]==0 and len(nums)==1:
        #     return False

        # summ=0
        # diff=-1
        # index=[]

        # for i in range(len(nums)):
        #     index.append(i)
        # index.sort(reverse=True)

        # for i in range(len(nums)):
        #     if nums[i]>=index[i]:
        #         return True

        # if nums[0]>=1:
        #     summ+=nums[0]
        #     diff=len(nums)-summ
        # else:
        #     return False

        # for _ in range(len(nums)):
        #     if summ<len(nums) and nums[summ]>=1:
        #         summ+=nums[summ]
        #         diff=len(nums)-summ
        #     if diff==0:
        #         return True
        
        # return False

        jump=0

        for i in range(len(nums)):
            if i>jump:
                return False
            jump=max(jump,i+nums[i])
        
        return True