import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = data[0]
for i in range(1, n):
    max_value = 0
    for j in range(i - 1, -1, -1):
        if data[j] < data[i]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + data[i]

# print(dp)
print(max(dp))