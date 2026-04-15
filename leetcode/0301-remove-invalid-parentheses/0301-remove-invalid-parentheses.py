class Solution:
    def removeInvalidParentheses(self, s):
        left=0 
        right=0
        
        for c in s:
            if c=='(':
                left+=1
            elif c==')':
                if left>0:
                    left-=1
                else:
                    right+=1

        res=set()

        def dfs(i,p,l,r,open):
            if i==len(s):
                if l==0 and r==0 and open==0:
                    res.add(p)
                return

            c=s[i]
            if c=='(' and l>0:
                dfs(i+1,p,l-1,r,open)
            elif c==')' and r>0:
                dfs(i+1,p,l,r-1,open)

            if c not in '()':
                dfs(i+1,p+c,l,r,open)
            
            elif c=='(':
                dfs(i+1,p+c,l,r,open+1)
            
            elif c==')' and open>0:
                dfs(i+1,p+c,l,r,open-1)
        
        dfs(0,"",left,right,0)
        return list(res)