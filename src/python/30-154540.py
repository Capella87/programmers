# 프로그래머스 30-154540 문제 : 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

xmove = [0, 1, 0, -1]
ymove = [1, 0, -1, 0]


def get_visitmap(height, width):
    rt = []
    for i in range(height):
        t = [False] * width
        rt.append(t)
    return rt


def bfs(mp, x, y, visitmap, width, height):
    rt = 0
    q = deque([])
    visitmap[x][y] = True
    deque.append(q, [x, y])
    rt += int(mp[x][y])
    while len(q) > 0:
        cur = deque.popleft(q)

        for i in range(4):
            new_x = cur[0] + xmove[i]
            new_y = cur[1] + ymove[i]
            if new_x < 0 or new_y < 0 or new_x >= height or new_y >= width:
                continue
            if visitmap[new_x][new_y] == False and mp[new_x][new_y] != 'X':
                visitmap[new_x][new_y] = True
                rt += int(mp[new_x][new_y])
                deque.append(q, [new_x, new_y])

    return rt


def solution(maps):
    answer = []
    width = len(maps[0])
    height = len(maps)
    visitmap = get_visitmap(height, width)

    for i in range(height):
        for j in range(width):
            if visitmap[i][j] == False and maps[i][j] != 'X':
                answer.append(bfs(maps, i, j, visitmap, width, height))
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
