def solution(research, n, k):
    answer = ''
    limit = 2 * n * k
    days = len(research)
    issue_index = days

    # list amount of day research and last index is number of issues
    word = {
        'a': [0 for _ in range(days + 1)],
        'b': [0 for _ in range(days + 1)],
        'c': [0 for _ in range(days + 1)],
        'd': [0 for _ in range(days + 1)],
        'e': [0 for _ in range(days + 1)],
        'f': [0 for _ in range(days + 1)],
        'g': [0 for _ in range(days + 1)],
        'h': [0 for _ in range(days + 1)],
        'i': [0 for _ in range(days + 1)],
        'j': [0 for _ in range(days + 1)],
        'k': [0 for _ in range(days + 1)],
        'l': [0 for _ in range(days + 1)],
        'm': [0 for _ in range(days + 1)],
        'n': [0 for _ in range(days + 1)],
        'o': [0 for _ in range(days + 1)],
        'p': [0 for _ in range(days + 1)],
        'q': [0 for _ in range(days + 1)],
        'r': [0 for _ in range(days + 1)],
        's': [0 for _ in range(days + 1)],
        't': [0 for _ in range(days + 1)],
        'u': [0 for _ in range(days + 1)],
        'w': [0 for _ in range(days + 1)],
        'x': [0 for _ in range(days + 1)],
        'y': [0 for _ in range(days + 1)],
        'z': [0 for _ in range(days + 1)]
    }

    day_count = 0
    for string in research:
        for alphabet in string:
            word[alphabet][day_count] += 1
        day_count += 1
    
    for key, value in word.items():
        issue_count = 0
        for i in range(days - n + 1):
            limit_check = 0
            for j in range(i, i + n):
                if value[j] < k:
                    break
                else:
                    limit_check += value[j]
            if limit_check >= limit:
                issue_count += 1
        value[issue_index] = issue_count

    best = 0
    best_key = ''
    for key, value in word.items():
        if value[issue_index] > best:
            best_key = key
            best = value[issue_index]
    if best == 0 :
        answer = "None"
    else:
        answer = best_key
    return answer

# solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"], 2, 2)
# solution(["yxxy","xxyyy"], 2, 1)
solution(["yxxy", "xxyyy", "yz"], 2, 1)