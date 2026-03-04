class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        p_sum=[0]*(len(s))

        for l,r,k in shifts:
            if k==1:
                if r+1<len(s):
                    p_sum[r+1]-=1
                p_sum[l]+=1
            else:
                if r+1<len(s):
                    p_sum[r+1]+=1
                p_sum[l]-=1
            
        c=[]

        for e in s:
            c.append(ord(e)-ord("a"))
        
        add=0

        for i in range(len(p_sum)):
            add+=p_sum[i]
            c[i]+=(add)

        res=[] 
        for i in range(len(c)):
            res.append(chr((c[i])%26 + 97))
        
        return "".join(res)
            
            