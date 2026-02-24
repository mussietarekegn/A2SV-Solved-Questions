class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        res=0

        while l<r:
            if height[l]<height[r]:
                area=height[l]*(r-l)
                l+=1
            else:
                area=height[r]*(r-l)
                r-=1
            res=max(res,area)
        
        return res
