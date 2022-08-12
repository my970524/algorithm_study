def solution(id_list, report, k):
#     report = list(set(report))
#     get_report = []
#     for i in report:
#         get_report.append(i.split(' ')[1])

#     suspended = []
#     for i in set(get_report):
#         if get_report.count(i) >= k:
#             suspended.append(i)

#     answer = [0 for _ in range(len(id_list))]
#     for i in range(len(id_list)):
#         for j in suspended:
#             if f'{id_list[i]} {j}' in report:
#                 answer[i] += 1
    report = set(report)
    answer = [0 for _ in range(len(id_list))]
    get_report = {}
    
    for i in id_list:
        get_report[i] = 0

    for i in report:
        a, b = i.split()
        get_report[b] += 1

    for i in report:
        a, b = i.split()
        if get_report[b] >= k:
            answer[id_list.index(a)] += 1

    return answer