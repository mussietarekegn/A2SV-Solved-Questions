class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp=defaultdict(int)

        for n in nums:
            mapp[n]+=1
        
        s= dict(sorted(mapp.items(), key=operator.itemgetter(1), reverse=True))

        ans=[]
        for key,val in s.items():
            if len(ans)<k:
                ans.append(key)
        
        return ans
