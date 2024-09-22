import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = []
pq = []

if n > 0:
	for _ in range(n):
		p, d = map(int, input().split())
		data.append((p, d))

	sorted_data = sorted(data, key=lambda x:(x[1], x[0]))

	for p, d in sorted_data:
		heapq.heappush(pq, p)
		while (len(pq) > d):
			heapq.heappop(pq)

print(sum(pq))