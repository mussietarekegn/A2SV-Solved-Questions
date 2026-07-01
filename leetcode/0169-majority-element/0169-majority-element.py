class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp = defaultdict(int)
        res = maxx = 0

        for i in range(len(nums)):
            mapp[nums[i]]+=1
            if maxx < mapp[nums[i]]:
                res = nums[i]
                maxx = mapp[nums[i]]

        return res

