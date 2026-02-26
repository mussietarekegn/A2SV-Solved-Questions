n,s=map(int,input().split())
arr=list(map(int,input().split()))

ans=0
l=0
summ=0

for i in range(n):
    summ+=arr[i]
    while summ>s:
        summ-=arr[l]
        l+=1
    ans=max(ans,i-l+1)

print(ans)
