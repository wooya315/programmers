def solution(n):
    change_n = list(str(n))
    change_n.reverse()
    return list(map(int, change_n))
