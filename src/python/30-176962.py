# 프로그래머스 30-176962 문제 : 과제 진행하기
# https://school.programmers.co.kr/learn/courses/30/lessons/176962

# 분류 : Heap, Greedy


import heapq
from collections import deque

def parse_time(strtime):
    splitted = strtime.split(':')
    return int(splitted[0]) * 60 + int(splitted[1])

def normalize_plans(plans):
    rt = []

    for i in plans:
        e = [parse_time(i[1]), int(i[2]), i[0]]
        heapq.heappush(rt, e)
    return rt


def solution(plans):
    answer = []

    planheap = normalize_plans(plans)
    unfinished = deque()
    cur_subject = heapq.heappop(planheap)
    while len(planheap) > 0:
        cur_end_time = cur_subject[0] + cur_subject[1]
        subject = cur_subject[2]
        if cur_end_time > planheap[0][0]:
            unfinished.appendleft((subject, cur_end_time - planheap[0][0]))
        elif cur_end_time == planheap[0][0]:
            answer.append(subject)
        else:
            answer.append(subject)
            if len(unfinished) > 0:
                stashed = deque.popleft(unfinished)
                cur_subject = [cur_end_time, stashed[1], stashed[0]]
                continue
        cur_subject = heapq.heappop(planheap)
    answer.append(cur_subject[2])
    while len(unfinished) > 0:
        answer.append(deque.popleft(unfinished)[0])

    return answer
