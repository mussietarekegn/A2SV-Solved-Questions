class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        for st in strs[1:]:
            i=0
            while i<len(pre) and i<len(st) and pre[i]==st[i]:
                i+=1
            pre=pre[:i]
            if not pre:
                return ""
        return pre
