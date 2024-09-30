import sys
input = sys.stdin.readline
data = []
n = int(input())
for _ in range(n):
    data.append(int(input()))

dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
    if i < 3:
        if i == 1:
            dp[i] = data[0] + data[1]
        else:
            dp[i] = max(data[0] + data[2], data[1] + data[2])
    else:
        dp[i] = data[i] + max(dp[i-2], dp[i-3] + data[i-1])

print(dp[n-1])