import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

def solution(priorities, location):
    answer = 0
    target = priorities[location]
    target_count = priorities.count(target)
    same_check = False
    if target_count > 1:
        same_check = True

    while True:
        max = heapsort(priorities)[0]
        head = priorities[0]
            
        if head != max:
            priorities.pop(0)
            priorities.append(head) 
            if location == 0:
                location = len(priorities)
        else:
            answer += 1
            priorities.pop(0)

            if same_check:
                if head == target and location == 0:
                    return answer
                elif head == target and location != 0:
                    return answer + location
            else:
                if head == target:
                    return answer

            if location == 0:
                location = len(priorities)

        location -= 1

# print(solution([5,9,1,3,5,7,5], 6))
# print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1, 1, 9, 1, 1], 4))