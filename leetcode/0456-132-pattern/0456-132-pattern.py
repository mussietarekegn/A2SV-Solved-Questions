class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s=float('-inf')
        stack=[]

        for i in range(len(nums)-1,-1,-1):
            if nums[i]<s:
                return True
            while stack and stack[-1]<nums[i]:
                s=stack.pop()
            stack.append(nums[i])
        return False
        
            
