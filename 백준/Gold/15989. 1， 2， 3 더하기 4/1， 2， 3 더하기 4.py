import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3

def get_2_3_combination(n):
    result = 0
    if n % 2 == 0:
        result += 1
    if n % 3 == 0:
        result += 1
    while n > 3:
        n -= 3
        if n % 2 == 0:
            result += 1
    return result


def get_result(n):
    for i in range(4, n+1):
        dp[i] = dp[i-1] + get_2_3_combination(i)
    return dp[n]


data = []
for _ in range(t):
    now = int(input())
    data.append(now)

max_num = max(data)

for i in range(4, max_num + 1):
    dp[i] = dp[i - 1] + get_2_3_combination(i)

for i in data:
    print(dp[i])


