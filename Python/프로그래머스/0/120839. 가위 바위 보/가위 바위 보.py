def solution(rsp):
    answer = ''
    temp = list(rsp)
    for i in temp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer