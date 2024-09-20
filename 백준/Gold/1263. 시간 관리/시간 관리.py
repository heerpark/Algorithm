import sys
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    ti, si = map(int, input().split())
    data.append((ti, si))

sorted_data = sorted(data, key=lambda x: x[1])

start_time = sorted_data[0][1] - sorted_data[0][0]
now_time = sorted_data[0][1]
sorted_data.pop(0)

# print(start_time, now_time)
for ti, si in sorted_data:
    if start_time < 0:
        start_time = -1
        break
    now_time += ti
    if now_time > si:
        start_time -= now_time - si
        now_time -= now_time - si
    # print(start_time, now_time)

print(start_time)