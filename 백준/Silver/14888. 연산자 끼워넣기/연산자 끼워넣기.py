import sys
n = int(input())
data = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

max_value = -1000000001
min_value = +1000000001

def dfs(i, now):
    global max_value, min_value, add, minus, mul, div
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - data[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])
print(max_value)
print(min_value)