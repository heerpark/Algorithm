n = int(input())

start = 0
end = n
temp = -1

if n == 0:
    now = 0

while start < end:
    now = int((start + end) / 2)
    if temp == now:
        now += 1
        break
    now_2 = now * now
    if now_2 == n:
        break
    elif now_2 > n:
        end = now
    else:
        start = now
    temp = now

print(now)