t = int(input())

for _ in range(t):
    n=int(input())
    a=input()
    b=input()

    bal=0
    gp=[False]*n
    for i in range(n):
        if a[i]=='0':
            bal+=1
        else:
            bal-=1
        
        if bal==0:
            gp[i]=True

    flip=False
    flag=True
    for i in range(n-1,-1,-1):
        curr=a[i]

        if flip:
            curr='1' if curr=='0' else '0'

        if curr!=b[i]:
            if not gp[i]:
                flag=False
                break
            flip=not flip

    if flag:
        print("YES")
    else:
        print("NO")
