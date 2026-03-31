class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]

        def helper(s):
            if len(s)==n:
                res.append(s)
                return
            for ch in ['a','b','c']:
                if not s or s[-1]!=ch:
                    helper(s+ch)
        helper("")
        if k<=len(res):
            return res[k-1]
        else:
            return ""