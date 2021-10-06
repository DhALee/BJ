import sys

n = int(sys.stdin.readline())
stack = []
answer = []
cur = 1
possible = True

for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        possible = False
        break

if possible:
    for i in answer:
        print(i)
