import string

temp = string.digits + string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0 :
        return temp[r] 
    else :
        return convert(q, base) + temp[r]

def prime(num):
    if num == 1 or num == 0 or (num % 2 == 0 and num > 2):
        return False
    else:
        for i in range(3, int(num**(1/2)) + 1, 2):
            if num % i == 0:
                return False
        return True

def solution(n, k):
    answer = 0
    converted_number = convert(n, k)
    seperated_numbers = list(str(converted_number).split('0'))
    seperated_numbers = [ i for i in seperated_numbers if i != '']
    # if '' in seperated_numbers:
    #     seperated_numbers.remove('')
    if len(seperated_numbers) > 0:
        for num in seperated_numbers:
            if prime(int(num)):
                answer += 1    
    return answer

solution(437674, 3)
solution(110011, 10)
solution(0, 10)