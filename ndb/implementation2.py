n = int(input())
h, m, s = 0, 0, 0
result = 0

for i in range(0, n+1):
    h = i
    for j in range(0, 60):
        m = j
        for k in range(0, 60):
            s = k
            check = str(h) + str(m) + str(s)
            if '3' in check:
                result += 1
            # print('{:02d} {:02d} {:02d}'.format(h, m, s))
print(result)