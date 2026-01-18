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


# def solution(spell, dic):
#     for d in dic:
#         if sorted(d) == sorted(spell):  # sorted의 결과는 리스트 형태라서 비교 가능
#             return 1
#     return 2