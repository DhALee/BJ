def solution(id_list, report, k):
    answer = []
    report_table = {name: [] for name in id_list}
    reported_table = {name: 0 for name in id_list}
    for names in report:
        n1, n2 = names.split()
        if n2 not in report_table[n1]:
            reported_table[n2] += 1
            report_table[n1].append(n2)

    reported_name = []
    for name, reported in reported_table.items():
        if reported >= k:
            reported_name.append(name)

    report_number = []
    for name, report in report_table.items():
        count = 0
        for name in reported_name:
            if name in report:
                count += 1
        report_number.append(count)

    # print(report_table)
    # print(reported_table)
    # print(reported_name)
    # print(report_number)
    answer = report_number
    return answer

# solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)