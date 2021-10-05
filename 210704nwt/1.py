array = input()
array = array.replace('[','')
array = array.replace(']','')
array = array.replace(',',' ')
array = list(map(int, array.split()))

id = [0] * 1000
check_first = [0] * 1000
sum = 0
winner = 0

for i in range(0, len(array), 2):
    id[array[i]] += 1
    if (array[i+1] == 1 and check_first[array[i]] == 0):
        check_first[array[i]] = 1
        sum += id[array[i]]
        winner += 1

if winner == 0:
    answer = 0
else:
    answer = int(sum // winner)

print(answer)