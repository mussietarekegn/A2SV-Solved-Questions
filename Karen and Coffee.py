n,k,q=map(int,input().split())
arr=[0]*(200002)

for _ in range(n):
    l,r=map(int,input().split())
    arr[l]+=1
    arr[r+1]-=1


for i in range(1,200001):
    arr[i]+=arr[i-1]

ad=[0]*(200001)

for i in range(1,200001):
    if arr[i]>=k:
        ad[i]=1

p_sum=[0]*(200001)

for i in range(1,200001):
    p_sum[i]=p_sum[i-1]+ad[i]

for _ in range(q):
    a,b=map(int,input().split())
    print(p_sum[b]-p_sum[a-1])

