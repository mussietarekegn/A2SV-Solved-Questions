n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if n%2==0:
    half=(n//2)-1
    print(arr[half])
else:
    half=(n//2)
    print(arr[half])
