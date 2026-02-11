class Solution:
    def frequencySort(self, s: str) -> str:
        cout=defaultdict(int)

        for i in range(len(s)):
            cout[s[i]]+=1

        rev= dict(sorted(cout.items(), key=lambda item: item[1], reverse=True))
        res=""

        for k,v in rev.items():
            res+=k*v
            
        return res
        
        
