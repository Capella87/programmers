# 프로그래머스 30-150370 문제 : 개인정보 수집 유효기간
# https://programmers.co.kr/learn/courses/30/lessons/150370
# 카테고리 : 코딩테스트 연습

# 2023 Kakao Blind Recruitment

def solution(today, terms, privacies):
    result = []
    trms = {}

    tyear, tmonth, tday = map(int, today.split('.'))
    tdate = (tyear - 2000 - 1) * 28 * 12 + (tmonth - 1) * 28 + tday
    for i in terms:
        t, m = i.split(' ')
        trms[t] = int(m) * 28

    orde = 1
    for pr in privacies:
        dat, p = pr.split(' ')
        y, m, dy = map(int, dat.split('.'))

        privacy_date = (y - 2000 - 1) * 28 * 12 + (m - 1) * 28 + dy + trms[p]

        if privacy_date <= tdate:
            result.append(orde)

        orde += 1

    return result
