class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]

        for i in range(1,len(strs)):
            curr = strs[i]
            j = 0
            newpre = ""

            while j<len(curr) and j<len(pre):
                if curr[j] == pre[j]:
                    newpre+= curr[j]
                else:
                    break
                j+=1
            pre = newpre

            if pre == "":
                return ""

        return pre    