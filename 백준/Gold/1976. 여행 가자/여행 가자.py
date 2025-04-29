import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


def find_parent(parent, a):
    if parent[a] != a:
        return find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

route = list(map(int, input().split()))

flag = True
for i in range(m-1):
    if find_parent(parent, route[i]) != find_parent(parent, route[i+1]):
        print("NO")
        flag = False
        break
if flag:
    print("YES")

