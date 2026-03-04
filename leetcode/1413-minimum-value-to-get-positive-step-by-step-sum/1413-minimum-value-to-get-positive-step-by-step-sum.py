class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        p_sum=[]
        add=0
        minn=1
        for i in range(len(nums)):
            add+=nums[i]
            minn=min(minn,add)
            p_sum.append(add)
        if minn>0:
            return minn
        else:
            j=0
            while j+minn<1:
                j+=1
            return j