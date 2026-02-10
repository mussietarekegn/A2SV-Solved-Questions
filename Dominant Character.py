from collections import Counter
t=int(input())

for _ in range(t):
    n=int(input())
    s=input()

    ans=float('inf')

    for  i in range(n):
        a=0
        b=0
        c=0
        for j in range(i,min(i+7,n)):
            if s[j]=="a":
                a+=1
            elif s[j]=="b":
                b+=1
            elif s[j]=="c":
                c+=1
            leng=j-i+1

            if leng>=2 and a>b and a>c:
                ans=min(ans,leng)

    if ans==float('inf'):
        print(-1)
    else:
        print(ans)
