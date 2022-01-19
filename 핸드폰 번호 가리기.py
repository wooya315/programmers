def solution(phone_number):
    slice_num = list(phone_number)[-4:]
    slice_num = ''.join(slice_num)
    change_num = list(phone_number)[:-4]
    a = len(change_num)
    a = '*'*a
    return a + slice_num
