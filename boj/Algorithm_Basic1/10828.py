import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command[:4] == "push":
        stack.append(int(command[5:]))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)