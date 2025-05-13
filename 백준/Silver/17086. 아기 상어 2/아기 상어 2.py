import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = []

INF = int(1e9)

def get_safe_distance(s_i, s_j, i, j):
    result = 0
    di = abs(s_i - i)
    dj = abs(s_j - j)
    if di == dj:
        return di
    elif di > dj:
        return di
    else:
        return dj

for _ in range(n):
    now = list(map(int, input().split()))
    data.append(now)

shark = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            shark.append((i, j))

global_result = 0

for i in range(n):
    for j in range(m):
        local_result = INF
        if (i, j) in shark:
            continue
        for s_i, s_j in shark:
            temp = get_safe_distance(s_i, s_j, i, j)
            # print("temp", temp, s_i, s_j, i, j)
            local_result = min(temp, local_result)
        global_result = max(global_result, local_result)
        # print("--------global-------", global_result)


print(global_result)