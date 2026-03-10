class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq=deque()
        maxq=deque()
        left=0
        ans=0

        for i in range(len(nums)):
            while minq and nums[minq[-1]]>nums[i]:
                minq.pop()
            while maxq and nums[maxq[-1]]<nums[i]:
                maxq.pop()
            minq.append(i)
            maxq.append(i)

            while abs(nums[minq[0]]-nums[maxq[0]])>limit:
                if minq[0]==left:
                    minq.popleft()
                if maxq[0]==left:
                    maxq.popleft()
                left+=1

            if nums[minq[0]]-nums[maxq[0]]<=limit:
                ans=max(ans,i-left+1)
        
        return ans
                
                    
