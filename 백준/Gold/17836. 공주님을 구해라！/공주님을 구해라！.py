from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

n, m, t = map(int, input().split())
grid = []

for _ in range(n):
    data = list(map(int, input().split()))
    grid.append(data)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            grid[i][j] = -1
        elif grid[i][j] == 2:
            grid[i][j] = -2

knife = 1000000
grid[0][0] = 1
queue.append((0, 0))
drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

while queue:
    row, col = queue.popleft()
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        cost = grid[row][col] + 1
        if 0 <= nrow < n and 0 <= ncol < m:
            if grid[nrow][ncol] == 0:
                grid[nrow][ncol] = cost
                queue.append((nrow, ncol))
            elif grid[nrow][ncol] == -2:
                grid[nrow][ncol] = cost
                knife = grid[nrow][ncol] + n - nrow - 1 + m - ncol - 1
                queue.append((nrow, ncol))


if grid[n-1][m-1] == 0:
    if knife == 1000000:
        print("Fail")
    elif knife - 1 <= t:
        print(knife - 1)
    else:
        print("Fail")
    
else:
    res = min(grid[n-1][m-1] - 1, knife - 1)
    if res <= t:
        print(res)
    else:
        print("Fail")





