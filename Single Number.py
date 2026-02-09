class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapp=defaultdict(int)

        for i in range(len(nums)):
            mapp[nums[i]]+=1
        
       

        for key,values in mapp.items():
            if values==1:
                return key
