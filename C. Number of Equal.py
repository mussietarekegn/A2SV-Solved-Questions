from collections import Counter
n,m=map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))

count1=Counter(arr1)
count2=Counter(arr2)
ans=0

for i in count1:
    if i in count2:
        ans+=count1[i]*count2[i]

print(ans)
