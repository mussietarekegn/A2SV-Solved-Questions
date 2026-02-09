class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        even_sum=0

        for j in range(len(nums)):
            if nums[j]%2==0:
                even_sum+=nums[j]   

        for i in range(len(queries)):
            que=queries[i]
            val,index=que
            if (nums[index]+val)%2==0:
                if nums[index]%2==0:
                    even_sum+=val
                else:
                    even_sum+=nums[index]+val
            else:
                if nums[index]%2==0:
                    even_sum-=nums[index]
            ans.append(even_sum)
            nums[index]=nums[index]+val
        
        return ans
            
            
        return ans
