import sys

n = int(sys.stdin.readline())

def vps(n):
    ps = []

    for _ in range(n):
        sum = 0
        ps = list(sys.stdin.readline().rstrip())
        if ps.count('(') != ps.count(')'):
            print("NO")
        else:
            for i in ps:
                if i == '(':
                    sum += 1
                else:
                    sum -= 1
                if sum < 0:
                    print("NO")
                    break
            if sum > 0:
                print("NO")
            elif sum == 0:
                print("YES")
    

vps(n)   