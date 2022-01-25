import math


def solution(progresses, speeds):
    answer = []
    takes = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]

    while len(takes) > 0:
        days = takes[0]
        takes = [a - days for a in takes]

        count = 0
        while count < len(takes) and takes[count] <= 0:
            count += 1

        takes = takes[count:]
        answer.append(count)

    return answer
