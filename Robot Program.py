t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    s=input()

    pos=x
    ti=float('inf')

    for i in range(n):
        if s[i]=='L':
            pos-=1
        else:
            pos+=1
        if pos==0:
            ti=i+1
            break
    
    if ti==float('inf') or ti>k:
        print(0)
        continue

    pos=0
    cycle=float('inf')

    for i in range(n):
        if s[i]=="L":
            pos-=1
        else:
            pos+=1
        if pos==0:
            cycle=i+1
            break
    
    ans=1
    r=k-ti
    if cycle!=float('inf'):
        ans+=r//cycle
    
    print(ans)
    
