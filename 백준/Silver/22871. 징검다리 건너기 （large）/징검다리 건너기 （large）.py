import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [float('inf')] * n

dp[0] = 0  # 첫 번째 돌은 힘이 0

for i in range(1, n):
    for j in range(i):
        force = (i - j) * (1 + abs(data[i] - data[j]))
        dp[i] = min(dp[i], max(dp[j], force))

print(dp[n-1])