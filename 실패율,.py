def solution(N, stages):
    answer = []
    a = len(stages)
    fail = {}
    for i in range(N):
        if a != 0:
            stage_fail = stages.count(i+1) / a
            a -= stages.count(i+1)
            fail[i+1] = stage_fail
        else:
            fail[i+1] = 0
    return sorted(fail, key=lambda x: fail[x], reverse=True)
