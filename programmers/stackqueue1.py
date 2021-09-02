## Best Solution ##
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]


from collections import deque
progress = deque()
speed = deque()
def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progress.append(progresses[i])
        speed.append(speeds[i])
     
    while len(progress) > 0:
        i = 0
        count = 0
        for j in speed:
            progress[i] += j
            i += 1

        for _ in range(len(progress)):
            if progress[0] >= 100:
                progress.popleft()
                speed.popleft()
                count += 1
            else:
                break
        if count != 0:
            answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
