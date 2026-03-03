t=int(input())

for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))

    p_sumr=[0]
    cur=0

    for i in range(n):
        cur+=r[i]
        p_sumr.append(cur)
    maxr=max(p_sumr)
    
    p_sumb=[0]
    cub=0

    for i in range(m):
        cub+=b[i]
        p_sumb.append(cub)
    
    maxb=max(p_sumb)
    if maxb+maxr>0:
        print(maxb+maxr)
    else:
        print(0)
