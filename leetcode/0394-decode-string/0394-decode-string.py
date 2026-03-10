class Solution:
    def decodeString(self, s: str) -> str:
        # stack=[]
        # num=[]
        # j=0
        # i=0
        # ans=[]
        # while i <len(s):
        #     if s[i].isdigit():
        #         j=i
        #         while s[i].isdigit():
        #             i+=1
        #         n=int(s[j:i])
        #         num.append(n)

        #     elif s[i]!="]":
        #         stack.append(s[i]) 
        #     else:
        #         alph=[]
        #         while stack[-1].isalpha():
        #             p=stack.pop()
        #             alph.append(p)
        #         alph.reverse()
        #         let="".join(alph)
        #         stack.pop()
        #         stack.append(let*num[-1])
        #         num.pop()
                
        #     i+=1
                
        # # ans.reverse()
        # return stack[-1]

        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                let=[]
                num=[]
                while stack and stack[-1].isalpha():
                    p=stack.pop()
                    let.append(p)
                let.reverse()
                let="".join(let)
                stack.pop()
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                k="".join(num)
                k=int(k)
                stack.append(k*let)
        return "".join(stack)


                
            


                    
