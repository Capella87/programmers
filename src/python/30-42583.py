# 프로그래머스 30-42583 문제 : 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
# 카테고리 : 코딩테스트 연습 > 스택/큐

from collections import deque


def solution(bridge_length, weight, truck_weights):
    elapsed = 0
    current_weight = 0
    trucks = len(truck_weights)
    bridge = deque()
    ord = 0
    passed = 0
    estimated_time_to_pass = deque()
    
    while passed < trucks:
        if len(estimated_time_to_pass) > 0 and estimated_time_to_pass[0] == elapsed:
            current_weight -= bridge.popleft()
            estimated_time_to_pass.popleft()
            passed += 1

        if ord < trucks and len(bridge) < bridge_length and truck_weights[ord] + current_weight <= weight:
            bridge.append(truck_weights[ord])
            estimated_time_to_pass.append(elapsed + bridge_length)
            current_weight += truck_weights[ord]
            ord += 1
        elapsed += 1
        
    return elapsed
