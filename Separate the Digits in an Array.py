class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        all=""

        for i in range(len(nums)):
            all+="".join(str(nums[i]))

        ans=[]

        for i in range(len(all)):
            ans.append(int(all[i]))
        
        return ans
