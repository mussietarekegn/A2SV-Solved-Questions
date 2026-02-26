n,s=map(int,input().split())
arr=list(map(int,input().split()))
 
summ=0
ans=float('inf')
l=0
 
for r in range(n):
    summ+=arr[r]
    while summ-arr[l]>=s:
        summ-=arr[l]
        l+=1
    if summ>=s:
        ans=min(ans,r-l+1)
 
if ans==float('inf'):
    print(-1)
    exit()
 
print(ans)
