# 프로그래머스 30-258711 문제 : 도넛과 막대 그래프
# https://programmers.co.kr/learn/courses/30/lessons/258711
# 카테고리 : 코딩테스트 연습

# 2024 Kakao Winter Internship

from collections import deque

def solution(edges):
    g = {}
    g_inbound = {}
    result = [0, 0, 0, 0]

    for e in edges:
        src = e[0]
        dest = e[1]

        g.setdefault(src, []).append(dest)
        g.setdefault(dest, [])
        g_inbound.setdefault(dest, []).append(src)
        g_inbound.setdefault(src, [])

    target = 0
    # Check the new vertex (No inbound edges) by inbound counts
    for i in g_inbound.keys():
        if len(g_inbound[i]) == 0 and len(g[i]) > 1:
            target = i
            break
    result[0] = target

    # Detect graph types
    is_visited = {i: False for i in g.keys()}

    for i in g[target]:
        find_graph_type(is_visited, g, g_inbound, result, i)

    return result


def find_graph_type(is_visited: dict, g: dict, g_inbound: dict, result: list, begin: int) -> None:
    stk = deque()
    is_visited[begin] = True
    stk.append(begin)
    cycles = 0
    while len(stk) > 0:
        v = stk.pop()

        if len(g[v]) == 0 and len(g_inbound[v]) > 0:
            result[2] += 1
            return
        if len(g[v]) == 2 and len(g_inbound[v]) >= 2:
            result[3] += 1
            return

        for i in g[v]:
            if not is_visited[i]:
                stk.append(i)
                is_visited[i] = True
            else:
                cycles += 1

    if cycles == 1:
        result[1] += 1
    elif cycles > 1:
        result[3] += 1
