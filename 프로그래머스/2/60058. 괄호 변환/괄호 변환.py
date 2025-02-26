def split_u_v(p):
    if not p:
        return "", ""
    count_open = 0
    count_close = 0
    for i in range(len(p)):
        if p[i] == '(':
            count_open += 1
        else:
            count_close += 1
        if count_open == count_close:
            u = p[:i+1]
            v = p[i+1:]
            return u, v
    return "", ""

def is_correct(p):
    if not p:
        return True
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            else:
                count -= 1
    if count == 0:
        return True
    else:
        return False

def get_bet_rev(p):
    if not p:
        return p
    res = ''
    if len(p) > 2:
        for i in range(1, len(p) - 1):
            if p[i] == '(':
                res = res + ')'
            else:
                res = res + '('
    return res

def solution(p):
    if not p:
        return p
    answer = ''
    u, v = split_u_v(p)
    if is_correct(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer = answer + solution(v)
        answer = answer + ')'
        answer = answer + get_bet_rev(u)
    return answer