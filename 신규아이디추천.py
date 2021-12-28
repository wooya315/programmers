import re


def solution(new_id):
    new_id = new_id.lower()
    lvl2 = re.compile('[0-9a-z_.\-]+')
    new_id = lvl2.findall(new_id)
    new_id = ''.join(new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    new_id = new_id.strip('.')
    if new_id == '':
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    if len(new_id) <= 2:
        idSize = len(new_id)
        addchar = new_id[idSize-1:]
        while len(new_id) < 3:
            new_id += addchar
    answer = new_id
    return answer
