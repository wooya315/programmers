def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2+1)):
        repeat = ''
        count = 1
        slice_string = s[:i]
        for j in range(i, len(s), i):
            count_string = s[j:j+i]
            if slice_string == count_string:
                count += 1
            else:
                if count != 1:
                    repeat = repeat + str(count) + slice_string
                else:
                    repeat = repeat + slice_string
                slice_string = s[j:j+i]
                count = 1
        if count != 1:
            repeat = repeat + str(count) + slice_string
        else:
            repeat = repeat + slice_string
        answer.append(len(repeat))
    return min(answer)
