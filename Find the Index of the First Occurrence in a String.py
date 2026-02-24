class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)

        for i in range(n-m+1):
            l=0
            while l<m and haystack[l+i]==needle[l]:
                l+=1
            if l==m:
                return i
        return -1
                
                
                
