import sys
input = sys.stdin.readline

n = int(input())
categorized = [0] * n
crain = list(map(int, input().split()))
crain.sort()
m = int(input())
box = list(map(int, input().split()))
time = 0

flag = False
for i in box:
    if i > crain[-1]:
        flag = True

for i in box:
    for j in range(len(crain)):
        if i <= crain[j]:
            categorized[j] += 1
            break

while sum(categorized) > 0:
    # print(categorized)
    for i in range(len(categorized)):
        if categorized[i] > 0:
            categorized[i] -= 1
        else:
            # print("hi")
            for j in range(i-1, -1, -1):
                # print("j:", j)
                if categorized[j] > 0:
                    categorized[j] -= 1
                    break
    # print("------------------")
    time += 1

if flag:
    print(-1)
else:
    print(time)