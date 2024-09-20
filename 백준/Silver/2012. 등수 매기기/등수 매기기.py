import sys

input = sys.stdin.readline

n = int(input())

list = []
res = 0
now = 1

for _ in range(n):
    a = int(input())
    list.append(a)

list.sort()

for i in list:
    res += abs(i - now)
    now += 1

print(res)