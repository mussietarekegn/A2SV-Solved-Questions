class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[]

        for i in range(n):
            nums.append(i+1)
        
        i=0
        while len(nums)>1:
            i=(k-1+i)%len(nums)
            nums.pop(i)

        return nums[-1]
        