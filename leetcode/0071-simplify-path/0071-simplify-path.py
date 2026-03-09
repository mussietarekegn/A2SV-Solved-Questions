class Solution:
    def simplifyPath(self, path: str) -> str:
        part=path.split('/')
        stack=[]
        print(part)

        for p in part:
            if p=="" or p==".":
                continue
            elif p=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        print(stack)
        
        return "/"+"/".join(stack)
        