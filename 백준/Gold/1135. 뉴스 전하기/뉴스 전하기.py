n = int(input())
data = list(map(int, input().split()))

rel = [[] for _ in range(n)]
cost = [0] * n

for i in range(n):
    if i > 0:
        rel[data[i]].append(i)

def get_min_cost(rel, cost, idx):
    temp = []
    for i in rel[idx]:
        temp.append(cost[i])
    temp.sort(reverse=True)
    for i in range(len(temp)):
        temp[i] += i
    return max(temp) + 1

def search(rel, cost, idx):
    if not rel[idx]:
        cost[idx] = 1
        return
    for i in rel[idx]:
        search(rel, cost, i)
    cost[idx] = get_min_cost(rel, cost, idx)

search(rel, cost, 0)

print(cost[0] - 1)