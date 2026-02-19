t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    c=[]
    for _ in range(n):
        l,r,real=map(int,input().split())
        c.append((l,r,real))
    
    c.sort()

    curr=k
    for l,r,real in c:
        if l>curr:
            break
        if curr<=r:
            curr=max(curr,real)

    print(curr)
