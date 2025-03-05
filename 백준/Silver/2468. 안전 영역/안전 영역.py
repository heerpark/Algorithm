import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

max_height = 0
for i in range(n):
    for j in range(n):
        max_height = max(max_height, data[i][j])

drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]

def get_safe_size(visited, row, col, num):
    q = deque()
    q.append((row, col))
    while q:
        now = q.popleft()
        if visited[now[0]][now[1]] != 0:
            continue
        visited[now[0]][now[1]] = num
        for i in range(4):
            nrow = now[0] + drow[i]
            ncol = now[1] + dcol[i]
            if 0 <= nrow < n and 0 <= ncol < n and visited[nrow][ncol] == 0:
                q.append((nrow, ncol))

result = 0

for i in range(0, max_height + 1):
    visited = [[-1] * (n) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if data[j][k] > i:
                visited[j][k] = 0
    # print("water", i)
    # for q in range(n):
    #     print(visited[q])
    num = 1
    for row in range(n):
        for col in range(n):
            if visited[row][col] == 0:
                get_safe_size(visited, row, col, num)
                num += 1
    # for q in range(n):
    #     print(visited[q])
    result = max(num - 1, result)
    # print("----------------")



print(result)

