def solution(student, k):
    answer = -1
    ob = 0
    yb = 0

    for i in student:
        if i == 1:
            ob += 1
    yb = len(student) - ob

    if ob < k :
        return 0        
    
    return answer