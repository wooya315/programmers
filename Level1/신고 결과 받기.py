def solution(id_list, report, k):
    report = set(report)
    who_declared = {}
    who_declare_who = {}
    stop_id = []
    answer = []
    for i in id_list:
        who_declared[i] = 0
        who_declare_who[i] = []
    # 신고를 당한 횟수 리스트 만들기
    for de in report:
        de = de.split(" ")
        user = de[0]
        survey = de[1]
        who_declared[survey] += 1
        who_declare_who[user] += [survey]
    # 정지되는 ID 리스트 만들기
    for key, value in who_declared.items():
        if value >= k:
            stop_id.append(key)
    for key, value in who_declare_who.items():
        stop_id.sort()
        value.sort()
        if value == stop_id and len(stop_id) >= k:
            answer.append(len(value))
        elif for i in value:
            if i in stop_id:
                answer.append(len(value))
        else:
            answer.append(0)
    return answer
