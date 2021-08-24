## List solution ##
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[len(participant)-1]


## Best solution ##
# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

def solution(participant, completion):
    dict = {}
    for name in participant:
        if dict.get(name):
            dict[name] += 1
        else:
            dict[name] = 1

    for name in completion:
        dict[name] -= 1

    for key in dict:
        if dict[key] > 0:
            return key


a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]
c = solution(a, b)
print(c)