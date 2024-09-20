import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())

if 2 * w < s:
    w_is_fast = True
else:
    w_is_fast = False

if x > y:
    long = x
    short = y
else:
    long = y
    short = x

res = 0

if w_is_fast:
    res = w * (x + y)
else:
    res = s * short
    long -= short
    while long >= 2:
        if w < s:
            res += 2 * w
        else:
            res += 2 * s
        long -= 2
    while long > 0:
        res += w
        long -= 1

print(res)

