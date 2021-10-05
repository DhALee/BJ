def solution(jobs):
    answer = []
    pick = 0
    num_jobs = len(jobs)
    available_jobs = []

    first_order = jobs[pick][0]
    now = jobs[pick][2]
    doing = jobs[pick][0]
    taking = jobs[pick][1]
    answer.append(jobs[pick][2])

    time_passed = 0
    last_order = jobs[num_jobs - 1][0]
    available_jobs.append(jobs[0])

    while last_order >= time_passed:
        doing = jobs[pick][0]
        while taking >= doing:
            
            doing += 1
        time_passed += 1

    return answer

solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])