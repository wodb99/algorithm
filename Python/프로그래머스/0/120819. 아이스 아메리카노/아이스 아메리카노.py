def solution(money):
    answer = []
    a = money // 5500
    answer.append(a)
    b = money % 5500
    answer.append(b)
    return answer