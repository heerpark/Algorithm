from collections import deque
import sys

input = sys.stdin.readline
queue = deque() #queue.append, queue.popleft()

n, m ,t = map(int, input().split())

data = []
drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            data[i][j] = -1
        elif data[i][j] == 2:
            data[i][j] = -2

# print(data)
knife = 100000
queue.append((0, 0))

while queue:
    row, col = queue.popleft()
    time = data[row][col] + 1
    for i in range(4):
        new_row = row + drow[i]
        new_col = col + dcol[i]
        if 0 <= new_row < n and 0 <= new_col < m:
            if data[new_row][new_col] >= 0:
                if data[new_row][new_col] == 0 or time < data[new_row][new_col]:
                    data[new_row][new_col] = time
                    queue.append((new_row, new_col))
            elif data[new_row][new_col] == -2:
                data[new_row][new_col] = time
                queue.append((new_row, new_col))
                knife = time
                knife += (n - new_row - 1) + (m - new_col - 1)

if data[n-1][m-1] == 0:
    if knife == 100000 or knife > t:
        print("Fail")
    else:
        print(knife)
else:
    res = min(knife, data[n-1][m-1])
    if res > t:
        print("Fail")
    else:
        print(res)

