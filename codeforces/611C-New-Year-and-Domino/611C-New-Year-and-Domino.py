h,w=map(int,input().split())
grid=[input() for _ in range(h)]

r=[[0]*w for _ in range(h)]
c=[[0]*w for _ in range(h)]


for i in range(h):
    for j in range(w):
        
        if j+1<w:
            if grid[i][j]=='.' and grid[i][j+1]=='.':
                r[i][j]=1
        if i+1<h:
            if grid[i][j]=='.' and grid[i+1][j]=='.':
                c[i][j]=1

p_sumr=[[0]*(w+1) for _ in range(h+1)]
p_sumc=[[0]*(w+1) for _ in range(h+1)]

for i in range(1,h+1):
    for j in range(1,w+1):
        p_sumr[i][j]=r[i-1][j-1]+p_sumr[i-1][j]+p_sumr[i][j-1]-p_sumr[i-1][j-1]
        p_sumc[i][j]=c[i-1][j-1]+p_sumc[i-1][j]+p_sumc[i][j-1]-p_sumc[i-1][j-1]

q=int(input())
for _ in range(q):
    r1,c1,r2,c2=map(int,input().split())
    t=0

    if c1<=c2-1:
        t+=p_sumr[r2][c2-1]-p_sumr[r1-1][c2-1]-p_sumr[r2][c1-1]+p_sumr[r1-1][c1-1]
    if r1<=r2-1:
        t+=p_sumc[r2-1][c2]-p_sumc[r1-1][c2]-p_sumc[r2-1][c1-1]+p_sumc[r1-1][c1-1]
    print(t)