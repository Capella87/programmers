// 프로그래머스 30-42587 문제 : 프린터
// https://programmers.co.kr/learn/courses/30/lessons/42587
// 카테고리 : 코딩테스트 연습 > 스택/큐

using System;
using System.Collections.Generic;

public class Solution
{
    public int solution(int[] priorities, int location)
    {
        int answer = 0;
        var q = new Queue<int>();
        int max = -1;
        int rank = 1;

        for (int i = 0; i < priorities.Length; i++)
        {
            q.Enqueue(i);
            if (max < priorities[i])
                max = priorities[i];
        }
        while (q.Count > 0)
        {
            int tIdx = q.Dequeue();
            if (max == priorities[tIdx])
            {
                if (tIdx == location)
                {
                    answer = rank;
                    break;
                }
                max = -1;
                for (int i = 0; i < q.Count; i++)
                {
                    tIdx = q.Dequeue();
                    if (max < priorities[tIdx])
                        max = priorities[tIdx];
                    q.Enqueue(tIdx);
                }
                rank++;
                continue;
            }
            q.Enqueue(tIdx);
        }
        return answer;
    }
}