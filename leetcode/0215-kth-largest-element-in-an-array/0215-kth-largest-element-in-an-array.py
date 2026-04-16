class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # idx=len(nums)-k
        
        # def quick(l,r):
        #     pivot=nums[r]
        #     p=l

        #     for i in range(l,r):
        #         if nums[i]<=pivot:
        #             nums[p],nums[i]=nums[i],nums[p]
        #             p+=1
            
        #     nums[p],nums[r]=nums[r],nums[p]

        #     if p>idx:
        #         return quick(l,p-1)
        #     elif p<idx:
        #         return quick(p+1,r)
        #     else:
        #         return nums[p]
        
        # return quick(0,len(nums)-1)
        nums.sort()
        return nums[-k]