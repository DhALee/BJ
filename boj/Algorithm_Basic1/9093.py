import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = list(sys.stdin.readline().split())
    for i in sentence:
        print(i[::-1], end=' ')
    print()
