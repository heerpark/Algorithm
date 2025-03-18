import sys
from collections import deque

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


def bfs(r, c, visited):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        nr, nc = q.popleft()
        for i in range(4):
            tr = nr + dr[i]
            tc = nc + dc[i]
            if 0 <= tr < n and 0 <= tc < m:
                if data[tr][tc] != 0 and not visited[tr][tc]:
                    visited[tr][tc] = True
                    q.append((tr, tc))


def is_all_melt():
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                return False
    return True


def get_melt_level(r, c):
    count = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if data[nr][nc] == 0:
                count += 1
    return count


def melt():
    temp = [[0] * m for _ in range(n)]  # 임시로 저장할 배열 생성
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                melt_value = get_melt_level(i, j)
                temp[i][j] = max(0, data[i][j] - melt_value)
    # 최종적으로 data에 반영
    for i in range(n):
        for j in range(m):
            data[i][j] = temp[i][j]


time = 0

while True:
    visited = [[False] * m for _ in range(n)]
    count = 0

    # 덩어리 개수 세기
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1

    if count >= 2:
        print(time)
        break

    if is_all_melt():
        print(0)
        break

    melt()
    time += 1
