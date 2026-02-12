class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq=Counter(nums)
        d=-1

        for k,v in freq.items():
            if v>len(nums)//2:
                d=k
                break
        
        if d==-1:
            return -1

        total=0

        for i in range(len(nums)):
            if nums[i]==d:
                total+=1
        
        l_count = 0
         
        for i in range(len(nums)-1):
            if nums[i] == d:
                l_count += 1
            r_count = total - l_count
            if r_count > (len(nums)-i-1)//2 and l_count > (i+1)//2:
                return i
        
        return -1
        


