n = int(input())
men = list(map(int, input().split()))
men.sort()
fear = 0
member = 0
count = 0
for i in men:
    fear += i
    member += 1
    if (fear // i) <= i and member == i:
        count += 1
        fear = 0
        member = 0
print(count)