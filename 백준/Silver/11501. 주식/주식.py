import sys
# 방법 1
# input = sys.stdin.readline
#
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     data = list(map(int, input().split()))
#     result = 0
#
#
#     for i in range(n-1):
#         now = data[i]
#         max_after_now = max(data[i+1:])
#         min_after_now = min(data[i+1:])
#         if min_after_now >= now:
#             result += max_after_now - now
#     print(result)

# 방법2
def calculate(start, end, max_data):
    result = 0
    for i in range(start, end):
        result += max_data - data[i]
    return result

def get_result(data):
    result = 0
    start = 0
    end = len(data)
    while start < end:
        max_data = max(data[start:end])
        max_index = data.index(max_data)
        result += calculate(start, max_index, max_data)
        start = max_index + 1
    return result

# 방법 3
def get_result(data, n):
    now_max = data[n-1]
    result = 0

    for i in range(n-1, -1, -1):
        if data[i] <= now_max:
            result += now_max - data[i]
        else:
            now_max = data[i]
    print(result)


t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    get_result(data, n)
