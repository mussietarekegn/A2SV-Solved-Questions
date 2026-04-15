def count(a,b,c):
    i=0
    j=b-1
    res=0

    while i<j:
        if a[i]+a[j]>c:
            res+=(j-i)
            j-=1
        else:
            i+=1
    return res

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0

    for k in range(2,n):
        if k<n-1:
            m=arr[n-1]
        else:
            m=arr[n-2]
        
        t=max(arr[k],m-arr[k])
        ans+=count(arr,k,t)
    print(ans)