# 프로그래머스 30-43105 문제 : 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 카테고리 : 코딩테스트 연습 > 동적계획법(Dynamic Programming)


def solution(triangle):
    bottom = len(triangle) - 1
    cache = triangle[bottom]
    
    for i in range(bottom - 1, -1, -1):
        for j in range(0, len(triangle[i])):
            cache[j] = triangle[i][j] + max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return cache[0]
