from collections import deque
import sys

input = sys.stdin.readline

def get_result(matrix):
    res = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if matrix[i][j][k] == 0:
                    return (-1)
                if matrix[i][j][k] > res:
                    res = matrix[i][j][k]
    return (res - 1)



def print_matrix_3d(matrix):
    for i in range(h):
        for j in range(n):
            print(matrix[i][j])
        print('-----------------')

m, n, h = map(int, input().split())
# n = row, m = col

matrix_3d = []
queue = deque()

for _ in range(h):
    matrix_2d = []
    for _ in range(n):
        matrix_1d = list(map(int, input().split()))
        matrix_2d.append(matrix_1d)
    matrix_3d.append(matrix_2d)

all_tomato = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix_3d[i][j][k] == 1:
                if matrix_3d[i][j][k] == 1:
                    queue.append((i, j, k))
            else:
                all_tomato = False

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

if not all_tomato:
    while queue:
        z, r, c = queue.popleft()
        day = matrix_3d[z][r][c] + 1

        if 0 <= z + 1 < h:
            if matrix_3d[z + 1][r][c] == 0 or day < matrix_3d[z + 1][r][c]:
                matrix_3d[z + 1][r][c] = day
                queue.append((z + 1, r, c))
        if 0 <= z - 1 < h:
            if matrix_3d[z - 1][r][c] == 0 or day < matrix_3d[z - 1][r][c]:
                matrix_3d[z - 1][r][c] = day
                queue.append((z - 1, r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if matrix_3d[z][nr][nc] == 0 or day < matrix_3d[z][nr][nc]:
                    matrix_3d[z][nr][nc] = day
                    queue.append((z, nr, nc))
    # print_matrix_3d(matrix_3d)
    print(get_result(matrix_3d))
else:
    print(0)

