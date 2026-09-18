from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    time = 0
    total_weight = 0
    
    while truck_weights:
        time += 1
        out = bridge.popleft()
        total_weight -= out
        
        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)
            
    return time + bridge_length