n=int(input())
arr=list(map(int,input().split()))

arr.sort()
day=0

for i in range(n):
    if arr[i]>=day+1:
        day+=1
        
print(day)
