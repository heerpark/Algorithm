import sys
from collections import deque
input = sys.stdin.readline


def get_data(n):
    data = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1
    # print("org graph", graph)
    # print("org indegree", indegree)
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if data.index(a) < data.index(b):
            indegree[a] += 1
            indegree[b] -= 1
            graph[a].remove(b)
            graph[b].append(a)
        else:
            indegree[a] -= 1
            indegree[b] += 1
            graph[b].remove(a)
            graph[a].append(b)
    return graph, indegree

# 동시에 나와도 안되고 q가 남아 있어도 안 됨.

def topology_sort(n):
    graph, indegree = get_data(n)
    q = deque()
    result = []
    append_count = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            append_count += 1
            q.append(i)
    if append_count > 1:
        return [-1]
    while q:
        append_count = 0
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                append_count += 1
        if append_count > 1:
            return [-1]
    if len(result) < n:
        return [-2]
    return result

n = int(input())
for _ in range(n):
    x = int(input())
    result = topology_sort(x)
    if result[0] == -1:
        print("?")
    elif result[0] == -2:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end=' ')
        print()