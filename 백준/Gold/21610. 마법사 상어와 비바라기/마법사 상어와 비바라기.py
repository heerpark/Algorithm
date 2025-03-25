n, m = map(int, input().split())

graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

moves = []
for _ in range(m):
    d, s = map(int, input().split())
    moves.append((d, s))

cloud = [[False] * n for _ in range(n)]

cloud[n-1][0] = True
cloud[n-1][1] = True
cloud[n-2][0] = True
cloud[n-2][1] = True


def moved_cloud(cloud, d, s, i, j):
    if d == 1:
        j -= s
    elif d == 2:
        i -= s
        j -= s
    elif d == 3:
        i -= s
    elif d == 4:
        i -= s
        j += s
    elif d == 5:
        j += s
    elif d == 6:
        i += s
        j += s
    elif d == 7:
        i += s
    elif d == 8:
        i += s
        j -= s
    i = i % n
    j = j % n
    # while not (0 <= i < n):
    #     if i < 0:
    #         i += 5
    #     else:
    #         i -= 5
    # while not (0 <= j < n):
    #     if j < 0:
    #         j += 5
    #     else:
    #         j -= 5
    return i, j


def move_clouds(cloud, d, s):
    bef = []
    new = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                bef.append((i, j))
                new_i, new_j = moved_cloud(cloud, d, s, i, j)
                new.append((new_i, new_j))
    for i, j in bef:
        cloud[i][j] = False
    for i, j in new:
        cloud[i][j] = True


def rain_and_copy_and_die(graph, cloud):
    temp = []
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    # 비 내리기
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                graph[i][j] += 1
                temp.append((i, j))

    # 물 복사 버그
    for i, j in temp:
        cnt = 0
        for k in range(4):
            ni = i + dr[k]
            nj = j + dc[k]
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] > 0:
                    cnt += 1
        graph[i][j] += cnt

    # 이전 구름을 모두 없애고
    prev_clouds = set(temp)
    for i in range(n):
        for j in range(n):
            cloud[i][j] = False

    # 새 구름 생성
    for i in range(n):
        for j in range(n):
            if (i, j) not in prev_clouds and graph[i][j] >= 2:
                cloud[i][j] = True
                graph[i][j] -= 2



# move_clouds(cloud, 1, 3)
# for i in range(n):
#     print(cloud[i])

def debug(graph, cloud):
    print("graph")
    for i in range(n):
        print(graph[i])
    print("cloud")
    for i in range(n):
        print(cloud[i])

def move(graph, cloud, d, s):
    move_clouds(cloud, d, s)
    rain_and_copy_and_die(graph, cloud)
    # debug(graph, cloud)


for d, s in moves:
    move(graph, cloud, d, s)

result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

# for i in range(n):
#     print(graph[i])

print(result)