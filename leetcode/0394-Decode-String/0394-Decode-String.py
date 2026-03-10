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