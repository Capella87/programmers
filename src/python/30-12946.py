# 프로그래머스 30-12946 문제 : 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946

# Recursion

def hanoi(n, src, via, dest, moves):
    if n == 1:
        moves.append([src, dest])
        return
    # Prior to move disk 'n' from src to dest, we have to move disk 'n - 1' from src to  via
    hanoi(n - 1, src, dest, via, moves)
    # Move disk 'n' from src to dest
    moves.append([src, dest])
    # Move disk 'n - 1' from via to dest
    hanoi(n - 1, via, src, dest, moves)

def solution(n):

    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer
