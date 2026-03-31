class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        ans=-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                r=mid-1   
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        arr=[]
        arr.append(ans)

        l=0
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                l=mid+1    
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
            
        arr.append(ans)
        return arr