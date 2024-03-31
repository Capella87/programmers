# 프로그래머스 30-42860 문제 : 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42860
# 카테고리 : 코딩테스트 연습 > 탐욕법(Greedy)

def solution(n: int, lost, reserve) -> int:
    status = [1] * n
    answer = n - len(lost)
    lost.sort()

    for i in lost:
        status[i - 1] = 0
    for i in reserve:
        status[i - 1] = 2 if status[i - 1] != 0 else 1

    for i in lost:
        if status[i - 1] == 1:
            answer += 1
            continue
        if i > 1 and status[i - 2] == 2:
            answer += 1
            status[i - 2] = status[i - 1] = 1
        elif i < n and status[i] == 2:
            answer += 1
            status[i] = status[i - 1] = 1

    return answer
