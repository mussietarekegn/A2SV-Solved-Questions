from collections import defaultdict
n,k=map(int,input().split())
arr=list(map(int,input().split()))

uni=0
freq=defaultdict(int)
l=0
ans=0

for r in range(n):
    if freq[arr[r]]==0:
        uni+=1
    freq[arr[r]]+=1

    while uni>k:
        freq[arr[l]]-=1
        if freq[arr[l]]==0:
            uni-=1
        l+=1
    ans+=r-l+1

print(ans)

