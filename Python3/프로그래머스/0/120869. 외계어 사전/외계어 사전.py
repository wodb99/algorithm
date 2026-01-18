def solution(spell, dic):
    answer = 0
    for word in dic:
        flag = 1
        for i in spell:
            if i not in word:
                flag = 0
                break
        if flag:
            answer = 1
            break
        else:
            answer = 2
    return answer