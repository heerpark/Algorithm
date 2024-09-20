import sys
import heapq
input = sys.stdin.readline

heap = []
data = []

n = int(input())

for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

sorted_data = sorted(data, key=lambda x: x[0])

for start, end in sorted_data:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))