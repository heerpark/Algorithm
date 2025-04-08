import sys

n, m, k = map(int, input().split())

a = []
for _ in range(n):
    data = list(map(int, input().split()))
    a.append(data)

power = [[5] * n for _ in range(n)]
graph = [[] * n for _ in range(n)]


for i in range(n):
    for _ in range(n):
        graph[i].append([])

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x-1][y-1].append(z)


dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]


def spring_and_summer():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 0:
                graph[i][j].sort()
                for k in range(len(graph[i][j])):
                    if power[i][j] - graph[i][j][k] >= 0:
                        power[i][j] -= graph[i][j][k]
                        graph[i][j][k] += 1
                    else:
                        dead_trees = graph[i][j][k:]
                        graph[i][j] = graph[i][j][:k]
                        for l in dead_trees:
                            power[i][j] += l // 2
                        break
                # print("summer", graph[i][j], dead_trees, power[i][j])

def autumn():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 0:
                for k in graph[i][j]:
                    if k % 5 == 0:
                        for l in range(8):
                            nr = i + dr[l]
                            nc = j + dc[l]
                            if 0 <= nr < n and 0 <= nc < n:
                                graph[nr][nc].append(1)
def winter():
    for i in range(n):
        for j in range(n):
            power[i][j] += a[i][j]

for _ in range(k):
    spring_and_summer()
    autumn()
    winter()

res = 0

for i in range(n):
    for j in range(n):
        if len(graph[i][j]) > 0:
            res += len(graph[i][j])

print(res)