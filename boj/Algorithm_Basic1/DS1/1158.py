import sys

n, k = map(int, sys.stdin.readline().split())
people = [i for i in range(1, n + 1)]
josephus = []
cur = 0

for t in range(n):
    cur += k - 1  
    if cur >= len(people):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        cur = cur % len(people)
    josephus.append(str(people.pop(cur)))

print("<", ", ".join(josephus), ">", sep="")