def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    for i in range(a-1):
        answer += month[i]

    answer += b - 1
    answer = answer % 7
    return day[answer]
