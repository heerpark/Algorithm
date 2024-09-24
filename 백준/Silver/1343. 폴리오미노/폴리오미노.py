data = input()
data = list(data)
count = 0
flag = False

for i in range(len(data)):
    if data[i] == 'X':
        count += 1
        if count == 2:
            data[i-1:i+1] = list("BB")
        if count == 4:
            data[i-3:i+1] = list("AAAA")
            count = 0
    else:
        if count % 2 != 0:
            flag = True
            break
        count = 0

if count % 2 != 0:
    flag = True

if flag:
    print(-1)
else:
    data = ''.join(data)
    print(data)