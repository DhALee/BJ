from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, target = map(int, input().split())
array = list(map(int, input().split()))

if count_by_range(array, target, target) == 0:
    print(-1)
else:
    print(count_by_range(array, target, target))