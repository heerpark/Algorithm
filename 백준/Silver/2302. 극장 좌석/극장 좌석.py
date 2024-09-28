import sys
input = sys.stdin.readline

res = 1

n = int(input())
dp = [0] * n
m = int(input())

for _ in range(m):
	vip = int(input())
	dp[vip - 1] = -1

count = 0
for i in range(n):
	count += 1
	if dp[i] == -1:
		if count > 1:
			res *= dp[i-1]
		count = 0
	elif count == 1:
		dp[i] = 1
	elif count == 2:
		dp[i] = 2
	elif count == 3:
		dp[i] = 3
	else:
		dp[i] = 2 * dp[i-2] + dp[i-3]

if dp[n-1] != -1:
	res *= dp[n-1]

print(res)