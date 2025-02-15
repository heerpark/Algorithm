import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(data, x, y):
    house = 1
    data[x][y] = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and data[new_x][new_y] == 1:
            house += dfs(data, new_x, new_y)
    return house

result = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            house = dfs(data, i, j)
            result.append(house)

result.sort()
print(len(result))
for i in result:
    print(i)



