arr=[]
for i in range(5):
    a=list(map(int,input().split()))
    arr.append(a)

ic=0
jr=0
tr=3
tc=3

for i in range(len(arr)):
    num=arr[i]
    for j in range(len(num)):
        if num[j]==1:
            ic=j+1
            jr=i+1

ans=abs((tr-jr))+abs(tc-ic)
print(ans)
            
