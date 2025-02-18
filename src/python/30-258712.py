# 프로그래머스 30-258712 문제 : 가장 많이 받은 선물
# https://programmers.co.kr/learn/courses/30/lessons/258712

def update_stat(gift_dashboard, total_gave, total_received, giver_idx, receiver_idx):
    # [giver][receiver]
    gift_dashboard[giver_idx][receiver_idx] += 1
    total_gave[giver_idx] += 1
    total_received[receiver_idx] += 1


def solution(friends, gifts):
    le = len(friends)

    friends_idx = {}
    idx = 0
    # Be careful to Pythonnic initialization
    gift_dashboard = [[0] * le for _ in range(le)]
    total_received = [0] * le
    total_gave = [0] * le
    gift_index = [0] * le
    result = [0] * le
    mx = 0

    for f in friends:
        friends_idx[f] = idx
        idx += 1

    for trf in gifts:
        rcrd = trf.split(' ')
        giver = rcrd[0]
        receiver = rcrd[1]
        giver_key = friends_idx[giver]
        receiver_key = friends_idx[receiver]
        update_stat(gift_dashboard, total_gave, total_received, giver_key, receiver_key)
        # Calc gift-index
    for i in range(le):
        gift_index[i] = total_gave[i] - total_received[i]

    # Calc additional gifts for each person
    for i in range(le - 1):
        # i <= A, j <= B
        for j in range(i + 1, le):
            if gift_dashboard[i][j] > gift_dashboard[j][i]:
                result[i] += 1
            elif gift_dashboard[i][j] < gift_dashboard[j][i]:
                result[j] += 1
            elif gift_index[i] > gift_index[j]:
                result[i] += 1
            elif gift_index[i] < gift_index[j]:
                result[j] += 1
    result.sort()
    print(result)
    return result[-1]
