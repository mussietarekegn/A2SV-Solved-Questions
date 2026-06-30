class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            
            for ch in word:
                freq[ord(ch) - ord("a")]+=1
            
            key = tuple(freq)
            mapp[key].append(word)
        
        return list(mapp.values())