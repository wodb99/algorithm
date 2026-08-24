def solution(numlist, n):
    answer = []
    diff = []
    for i in numlist:
        dist = abs(n - i)
        # 밑에서의 정렬은 오름차순인데, 거리가 같다면 큰 수가 앞에 오도록 배치해야하기 때문에 - 붙인 값을 함께 넣어줌
        diff.append((dist, -i, i)) 

    diff.sort()
    
    for a, b, c in diff:
        answer.append(c)
    
    return answer