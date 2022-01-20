# 내 풀이
def solution(s):
    answer = []
    upper = []
    for i in s:
        if i.islower() == True:
            answer.append(i)
            answer.sort(reverse=True)
        else:
            upper.append(i)
            upper.sort(reverse=True)
    answer = "".join(answer)
    upper = "".join(upper)
    return answer + upper

# 다른 사람 풀이


def solution(s):
    return (''.join(sorted(s)[::-1]))
