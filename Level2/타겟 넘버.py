from collections import deque


def solution(numbers, target):
    answer = 0
    deq = deque()
    n = len(numbers)
    deq.append([numbers[0], 0])
    deq.append([-1*numbers[0], 0])
    while deq:
        temp, level = deq.popleft()
        level += 1
        if level < n:
            deq.append([temp+numbers[level], level])
            deq.append([temp-numbers[level], level])
        else:
            if temp == target:
                answer += 1
    return answer
