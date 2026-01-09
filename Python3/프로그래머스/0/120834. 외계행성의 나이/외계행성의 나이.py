def solution(age):
    answer = ''
    temp = list('abcdefghij')
    idx = list(str(age))
    for i in idx:
        answer += temp[int(i)]
    return answer