def solution(my_string):
    answer = ''
    temp = []
    sent = list(my_string)
    for i in sent:
        if i not in temp:
            temp.append(i)
        else:
            continue
    for j in temp:
        answer += j
    return answer