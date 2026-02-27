t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=input()

    l=0
    ans=float('inf')
    nb=0
    nw=0

    for r in range(n):
        if arr[r]=='B':
            nb+=1
        else:
            nw+=1
        while r-l+1>k:
            if arr[l]=='B':
                nb-=1
            else:
                nw-=1
            l+=1
        if nw+nb==k:
            ans=min(ans,nw)
    
    if ans==float('inf') or ans<0:
        print(0)
    else:
        print(ans)
