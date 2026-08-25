from collections import defaultdict

def solution(participant, completion):
    check = defaultdict(int)
    for name1 in participant:
        check[name1] += 1
    for name2 in completion:
        check[name2] -= 1
    for name, val in check.items(): # 키와 값을 같이 가져오려면 .items() 이용
        if val > 0:
            return name