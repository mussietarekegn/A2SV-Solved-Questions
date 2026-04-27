class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)
        
        gap = math.ceil((max_val - min_val) / (n - 1))
        
        buckets_min = [float('inf')] * (n - 1)
        buckets_max = [float('-inf')] * (n - 1)
        
        for num in nums:
            if num == min_val or num == max_val:
                continue
            
            idx = (num - min_val) // gap
            
            buckets_min[idx] = min(num, buckets_min[idx])
            buckets_max[idx] = max(num, buckets_max[idx])

        max_gap = 0
        prev = min_val
        
        for i in range(n - 1):
            if buckets_min[i] == float('inf'):
                continue
            
            max_gap = max(max_gap, buckets_min[i] - prev)
            prev = buckets_max[i]
        
        max_gap = max(max_gap, max_val - prev)
        
        return max_gap