// 프로그래머스 30-42840 문제 : 모의고사
// https://programmers.co.kr/learn/courses/30/lessons/42840
// 카테고리 : 코딩테스트 연습 > 완전탐색

function solution(answers) {
    const rt = [];
    
    const first = [1, 2, 3, 4, 5];
    const second = [2, 1, 2, 3, 2, 4, 2, 5];
    const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    const correctCount = [0, 0, 0];
    
    for (let i = 0; i < answers.length; i++) {
        if (first[i % 5] == answers[i]) correctCount[0]++;
        if (second[i % 8] == answers[i]) correctCount[1]++;
        if (third[i % 10] == answers[i]) correctCount[2]++;
    }
    
    let max = 0;
    for (let i = 0; i < 3; i++) {
        if (max < correctCount[i])
            max = correctCount[i];
    }
    for (let i = 0; i < 3; i++) {
        if (max == correctCount[i]) {
            rt.push(i + 1);
        }
    }
    
    return rt;
}