# 프로그래머스 30-131118 문제 : 서울에 위치한 식당 목록 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/131118
# 카테고리 : 코딩테스트 연습 > SELECT (SQL)

# First Solution with Subquery
BEGIN
SELECT REST_INFO.REST_ID, 
       REST_INFO.REST_NAME,
       REST_INFO.FOOD_TYPE,
       REST_INFO.FAVORITES,
       REST_INFO.ADDRESS,
       RR.SCORE AS 'SCORE'
       FROM REST_INFO
       JOIN (SELECT REST_REVIEW.REST_ID, 
                   ROUND(AVG(REST_REVIEW.REVIEW_SCORE), 2) AS 'SCORE'
                    FROM REST_REVIEW
                    GROUP BY REST_REVIEW.REST_ID
                    ) AS RR
                    ON REST_INFO.REST_ID = RR.REST_ID
       WHERE REST_INFO.ADDRESS LIKE '서울%'
       ORDER BY RR.SCORE DESC, REST_INFO.FAVORITES DESC;
END

# Second Solution without Subquery
BEGIN
SELECT REST_REVIEW.REST_ID, REST_INFO.REST_NAME, REST_INFO.FOOD_TYPE, REST_INFO.FAVORITES,
      REST_INFO.ADDRESS, ROUND(AVG(REST_REVIEW.REVIEW_SCORE), 2) AS 'SCORE'
    FROM REST_REVIEW
    INNER JOIN REST_INFO ON REST_REVIEW.REST_ID = REST_INFO.REST_ID
    GROUP BY REST_REVIEW.REST_ID
    HAVING REST_INFO.ADDRESS LIKE '서울%'
    ORDER BY SCORE DESC, REST_INFO.FAVORITES DESC
END