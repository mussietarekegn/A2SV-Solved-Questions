if __name__ == '__main__':
    n = int(input())
    arr=[]
    
    for i in range(n):
        arr.append(i*i)
    
    for i in range(len(arr)):
        print(arr[i])
