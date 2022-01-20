def solution(n):
    change_n = list(str(n))
    s_n = sorted(change_n, reverse=True)
    return int("".join(s_n))
