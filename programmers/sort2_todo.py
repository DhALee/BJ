def stringSort(n1, n2):
    n1_len = len(n1)
    n2_len = len(n2)
    if (n1_len == n2_len) and n1_len == 1:
        return n1, n2
    elif n1_len == n2_len and n1_len > 1:
        for i in range(1, n1_len):
            if int(n1[i]) > int(n2[i]):
                return n1, n2
            elif int(n1[i]) < int(n2[i]):
                return n2, n1
            elif int(n1[i]) == int(n2[i]):
                if i == n1_len - 1:
                    return n1, n2
                else:
                    continue
    elif n1_len > n2_len:
        for i in range(1, n2_len):
            if int(n1[i]) > int(n2[i]):
                return n1, n2
            elif int(n1[i]) < int(n2[i]):
                return n2, n1
            elif int(n1[i]) == int(n2[i]):
                continue
        for i in range(n2_len, n1_len):
            if int(n1[i]) > int(n2[n2_len - 1]):
                return n1, n2
            elif int(n1[i]) < int(n2[n2_len - 1]):
                return n2, n1
            elif int(n1[i]) == int(n2[n2_len - 1]):
                if i == n1_len - 1:
                    return n1, n2
                    # if int(n2[n2_len - 2]) >= int(n2[n2_len - 1]):
                    #     return n1, n2
                    # else:
                    #     return n2, n1
                else:
                    continue
    elif n1_len < n2_len:
        for i in range(1, n1_len):
            if int(n1[i]) > int(n2[i]):
                return n1, n2
            elif int(n1[i]) < int(n2[i]):
                return n2, n1
            elif int(n1[i]) == int(n2[i]):
                continue
        for i in range(n1_len, n2_len):
            if int(n1[n1_len - 1]) > int(n2[i]):
                return n1, n2
            elif int(n1[n1_len - 1]) < int(n2[i]):
                return n2, n1
            elif int(n1[n1_len - 1]) == int(n2[i]):
                if i == n2_len - 1: 
                    return n2, n1
                    # if int(n1[n1_len - 2]) >= int(n1[n1_len - 1]):
                    #     return n1, n2
                    # else:
                    #     return n2, n1
                else:
                    continue

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(arr[j][0]) < int(arr[j + 1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif int(arr[j][0]) == int(arr[j + 1][0]):
                arr[j], arr[j + 1] = stringSort(arr[j], arr[j + 1])

def solution(numbers):
    answer = ''
    string_numbers = []
    for number in numbers:
        string_numbers.append(str(number))

    dictionary = {number : int(number[0]) for number in string_numbers}
    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
    sorted_numbers = list(dictionary.keys())
    # print(sorted_numbers)
    bubbleSort(sorted_numbers)    
    for number in sorted_numbers:
        answer += number
    # print(answer)
    return answer



# solution([7, 6, 3, 30, 34, 5, 9])


# Need to fix when stringSort get numbers like these test cases below
solution([30, 3003]) # 303003
solution([30, 3000]) # 303000
solution([34444, 34]) # 3444434
