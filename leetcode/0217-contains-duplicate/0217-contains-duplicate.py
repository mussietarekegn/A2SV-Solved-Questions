class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp = defaultdict(int)
        for num in nums:
            mapp[num]+= 1
        
        for val in mapp.values():
            if val>1:
                return True
        return False
        