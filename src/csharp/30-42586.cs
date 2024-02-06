// 프로그래머스 30-42586 문제 : 기능개발
// https://school.programmers.co.kr/learn/courses/30/lessons/42586
// 카테고리 : 코딩테스트 연습 > 스택/큐 (Stack/Queue)

using System;
using System.Collections.Generic;

public class Solution
{
    public int[] solution(int[] progresses, int[] speeds)
    {
        int currentIdx = 0;
        int dist_count, days = 0;
        var distributions = new List<int>();
        
        while (currentIdx < progresses.Length)
        {
            dist_count = 1;
            while (progresses[currentIdx] < 100)
            {
                progresses[currentIdx] += speeds[currentIdx];
                days++;
            }
            
            while (++currentIdx < progresses.Length)
            {
                progresses[currentIdx] += speeds[currentIdx] * days;
                if (progresses[currentIdx] < 100)
                {
                    break;
                }
                dist_count++;
            }
            distributions.Add(dist_count);
        }
        
        return distributions.ToArray();
    }
}
