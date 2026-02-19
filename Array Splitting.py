n,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

if k==1:
    print(arr[-1]-arr[0])
else:
    diff=[]
    for i in range(1,len(arr)):
        diff.append(arr[i]-arr[i-1])
    
    diff.sort(reverse=True)
    
    split=sum(diff[:k-1])

    total=arr[-1]-arr[0]
    print(total-split)
