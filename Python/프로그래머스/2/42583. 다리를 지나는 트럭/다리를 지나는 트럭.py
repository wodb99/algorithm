def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length  # 다리를 리스트로 표현
    onbridge = sum(bridge)   # 현재 다리 위의 무게
    
    while bridge:
        answer += 1
        onbridge -= bridge.pop(0)   # 맨 앞 트럭 내리기
        
        if truck_weights:   # 아직 대기 트럭이 있다면
            if onbridge + truck_weights[0] <= weight:   # 새 트럭 올릴 수 있는지 검사
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)
                onbridge += new_truck
            
            else:
                bridge.append(0)   # 시간 흐름에 따른 이동
    
    return answer