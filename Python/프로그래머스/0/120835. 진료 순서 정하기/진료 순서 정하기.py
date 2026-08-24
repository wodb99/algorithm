def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    
    for i in emergency:
        a = temp.index(i)
        answer.append(a + 1)
    return answer