# 프로그래머스 30-86971 문제 : 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

# Exhaustive Search

from collections import deque


def create_visitstatus(n):
    rt = [0] * (n + 1)
    return rt

def bfs(tree, start_node, cut_edge, is_visited):
    q = deque([start_node])
    is_visited[start_node] = 1
    deque.append(q, start_node)
    st_nodes = 1
    while len(q) > 0:
        node = deque.popleft(q)
        for i in tree[node]:
            if (node == cut_edge[0] and i == cut_edge[1]) or (node == cut_edge[1] and i == cut_edge[0]):
                continue
            if is_visited[i] == 0:
                is_visited[i] = 1
                st_nodes += 1
                deque.append(q, i)
    return st_nodes


def divide_grid(tree, connection, node_count):
    is_visited = create_visitstatus(node_count)
    lft = bfs(tree, connection[0], connection, is_visited)
    rght = bfs(tree, connection[1], connection, is_visited)
    return abs(lft - rght)


def solution(n, wires):
    answer = -1

    # 트리 구축
    tr = [[] for i in range(n + 1)]
    for conn in wires:
        tr[conn[0]].append(conn[1])
        tr[conn[1]].append(conn[0])
    for conn in wires:
        temp = divide_grid(tr, conn, len(tr))
        if answer == -1 or temp < answer:
            answer = temp

    return answer
