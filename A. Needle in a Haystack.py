from collections import Counter
t=int(input())

for _ in range(t):
    s=input()
    s2=input()

    counts=Counter(s)
    countt=Counter(s2)
    
    flag=True
    for ch in counts:
        if counts[ch]>countt[ch]:
            flag=False
    
    if not flag:
        print("Impossible")
        continue
    else:
        for ch in s:
            countt[ch]-=1
        r=[]
        for ch in sorted(countt):
            r.append(ch*countt[ch])
        
        r="".join(r)
        l=0
        res=[]

        for ch in r:
            while l<len(s) and s[l]<=ch:
                res.append(s[l])
                l+=1
            res.append(ch)

        while l<len(s):
            res.append(s[l])
            l+=1
        
        print("".join(res))



