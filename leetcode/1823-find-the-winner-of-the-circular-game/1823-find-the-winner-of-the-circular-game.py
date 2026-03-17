class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # d=set()

        # arr=[]
        # for i in range(n):
        #     arr.append(i+1)
        
        # arr2=(arr)*k
        # print(arr2)
        # count=0
        # for i in range(len(arr2)):
        #     if arr2[i] in d:
        #         continue
        #     count+=1
        #     if len(d)+1==len(arr):
        #         break
        #     if count==k:
        #         d.add(arr2[i])
        #         count=0
        # print(d)
        # for i in range(len(arr)):
        #     if arr[i] not in d:
        
        #         return arr[i]


        def helper(nums,k,ind):
            if len(nums)==1:
                return nums[0]
            i=(k-1+ind)%len(nums)
            nums.pop(i)
            return helper(nums,k,i)
        
        nums=[]
        for i in range(n):
            nums.append(i+1)
        
        return helper(nums,k,0)
        