location = input()
row = int(location[1])
column = location[0]
column = int(ord(column)) - int(ord('a')) + 1

# knight movements -> E*2, W*2, S*2, N*2
# dx = [2, 2, -2, -2, 1, -1, 1, -1]
# dy = [1, -1, 1, -1, -2, -2, 2, 2]
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    new_row = row + step[0]
    new_column = column + step[1]
    if new_row >= 1 and new_row <= 8 and new_column >= 1 and new_column <= 8:
        result += 1

print(result)