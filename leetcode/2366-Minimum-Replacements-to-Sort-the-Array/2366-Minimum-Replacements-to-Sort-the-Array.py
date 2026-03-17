class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        el=nums[-1]
        oper=0

        for i in range(len(nums)-1,-1,-1):
            if el<nums[i]:
                part=ceil(nums[i]/el)
                nums[i]=nums[i]//part
                oper+=part-1
            el=nums[i]

        return oper