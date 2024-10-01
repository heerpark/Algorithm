import sys
input = sys.stdin.readline

n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)
time = 0

if crain[0] < box[0]:
    time = -1
else:
    while box:
        for i in crain:
            if box and i < box[-1]:
                continue
            for j in box:
                if j <= i:
                    box.remove(j)
                    break
        time += 1

print(time)



