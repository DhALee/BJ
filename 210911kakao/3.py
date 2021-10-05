import math

def convert(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)

def solution(fees, records):
    answer = []
    log = {}

    for record in records:
        time, number, io = record.split()
        log[number] = []
    for record in records:
        time, number, io = record.split()
        log[number].append(time)

    total = {}
    for number, time in log.items():
        io_num = len(time)
        total_time = 0
        max_time = False
        if io_num % 2 != 0:
            max_time = True
        if max_time:
            for i in range(0, io_num - 1, 2):
                total_time += convert(time[i + 1]) - convert(time[i])
            total_time += convert("23:59") - convert(time[io_num - 1])
            total[number] = total_time
        else:
            for i in range(0, io_num, 2):
                total_time += convert(time[i + 1]) - convert(time[i])
            total[number] = total_time

    price = {}
    for number, total in total.items():
        if total <= fees[0]:
            price[number] = fees[1]
        else:
            total -= fees[0]
            extra_pay = math.ceil(total/fees[2]) * fees[3]
            price[number] = fees[1] + extra_pay
    # print(log)
    # print(total)
    for k, v in sorted(price.items()):
        answer.append(v)
    print(answer)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
# solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])

# print(convert("05:34"))