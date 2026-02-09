class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp=defaultdict(list)
        ans=[]

        for word in strs:
            key="".join(sorted(word))
            mapp[key].append(word)

        for values in mapp.values():
            ans.append(values)

        return ans            
