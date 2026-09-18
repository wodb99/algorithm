def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_score, b_score, c_score = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a[(5 + i) % 5]:
            a_score += 1
        if answers[i] == b[(8 + i) % 8]:
            b_score += 1
        if answers[i] == c[(10 + i) % 10]:
            c_score += 1
    
    max_v = max(a_score, b_score, c_score)
    temp = [a_score, b_score, c_score]
    for idx in range(3):
        if max_v == temp[idx]:
            answer.append(idx + 1)            
            
    return answer