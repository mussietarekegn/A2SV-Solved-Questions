class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        
        perm=self.permute(nums[1:])
        res=[]

        for p in perm:
            for i in range(len(p)+1):
                p_=p.copy()
                p_.insert(i,nums[0])
                res.append(p_)
        return res