class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapp=defaultdict(int)

        for i in range(len(nums)):
            mapp[nums[i]]+=1
        
        ans=[]

        for key,values in mapp.items():
            if values>len(nums)/3:
                ans.append(key)

        return ans
