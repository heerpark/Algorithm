import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
pq = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

data.sort(key=lambda x: x[0])

for i in data:
    if len(pq) > 0:
        if i[0] >= pq[0]:
            heapq.heappop(pq)
    heapq.heappush(pq, i[1])

print(len(pq))


