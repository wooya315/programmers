def solution(x, n):
    answer = []
    for i in range(1, 1001):
        if len(answer) < n:
            answer.append(x*i)
    return answer
