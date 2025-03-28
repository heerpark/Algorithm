import sys

input = sys.stdin.readline
INF = 1000000000
n = int(input())

data = list(map(int, input().split()))

dp = [INF] * n
dp[0] = 0

for j in range(n):
    for i in range(j):
        power = (j - i) * (1 + abs(data[i] - data[j]))
        dp[j] = min(dp[j], max(dp[i], power))


print(dp[n-1])