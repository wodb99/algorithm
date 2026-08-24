from statistics import mean

def solution(score):
    answer = []
    avg = []
    for student in score:
        avg.append(mean(student))
    temp = sorted(avg, reverse=True)
    for i in avg:
        answer.append(temp.index(i) + 1)
    return answer