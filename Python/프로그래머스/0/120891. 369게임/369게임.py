def solution(order):
    answer = 0
    clap = ['3', '6', '9']
    temp = list(str(order))
    for i in temp:
        if i in clap:
            answer += 1
    return answer