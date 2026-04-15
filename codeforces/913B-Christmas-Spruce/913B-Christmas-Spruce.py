from collections import defaultdict

n = int(input())
tree = defaultdict(list)

for i in range(2, n + 1):
    p = int(input())
    tree[p].append(i)

is_leaf = [False] * (n + 1)

for i in range(1, n + 1):
    if len(tree[i]) == 0:
        is_leaf[i] = True

for i in range(1, n + 1):
    if len(tree[i]) > 0:
        cnt = 0
        for child in tree[i]:
            if is_leaf[child]:
                cnt += 1
        
        if cnt < 3:
            print("No")
            exit()

print("Yes")