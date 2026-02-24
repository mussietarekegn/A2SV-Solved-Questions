t=int(input())
for _ in range(t):
    s=input()

    res=set()
    l=0
    i=0

    while i<len(s):
        l=i
        while l<len(s) and s[l]==s[i]:
            l+=1
        length=abs(l-i)

        if length%2==1:
            res.add(s[i])
        i=l
    
    ans=[]
    for ch in res:
        ans.append(ch)
    ans.sort()
    
    print("".join(ans))
