class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapp = set(nums)
        max_len = 0

        for num in mapp:
            if num-1 not in mapp:
                a = num
                leng = 1
                while a+1 in mapp:
                    a += 1
                    leng += 1

                max_len = max(max_len,leng)
            
            
        return max_len
