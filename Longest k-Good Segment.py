from collections import defaultdict

n,k=map(int,input().split())
arr=list(map(int,input().split()))

mapp=defaultdict(int)
uni=0
l=0
ans=0
al=0
ar=0

for r in range(n):
    if mapp[arr[r]]==0:
        uni+=1
    mapp[arr[r]]+=1
    while uni>k:
        mapp[arr[l]]-=1
        if mapp[arr[l]]==0:
            uni-=1
            mapp.pop(arr[l])
        l+=1
    if r-l+1>ans:
        ans=r-l+1
        al=l+1
        ar=r+1

print(al,ar)


