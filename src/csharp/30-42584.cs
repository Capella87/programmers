// 프로그래머스 30-42584 문제 : 주식가격
// https://programmers.co.kr/learn/courses/30/lessons/42584
// 카테고리 : 코딩테스트 연습 > 스택/큐

using System;

public class Solution
{   
    private int Count(int[] stk, int idx)
    {
        return 1 + idx;
    }
    
    private void Push(int[] stk, ref int idx, int target)
    {
        if (Count(stk, idx) < stk.Length)
        {
            stk[++idx] = target;
        }
    }
    
    private int Pop(int[] stk, ref int idx)
    {
        if (idx > -1)
        {
            int rt = stk[idx--];
            
            return rt;
        }
        
        return -1;
    }
    
    private int Top(int[] stk, int idx)
    {
        return idx > -1 ? stk[idx] : -1;
    }
    
    public int[] solution(int[] prices)
    {
        int[] _arrStk = new int[prices.Length];
        int idx = -1, topIdx = 0, last = prices.Length - 1;
        int[] answer = new int[prices.Length];
        
        Push(_arrStk, ref idx, 0);
        
        for (int i = 1; i < prices.Length; i++)
        {
            topIdx = Top(_arrStk, idx);
            
            while (idx > -1 && prices[topIdx] > prices[i])
            {
                answer[topIdx] = i - topIdx;
                Pop(_arrStk, ref idx);
                topIdx = Top(_arrStk, idx);
            }
            
            Push(_arrStk, ref idx, i);
        }
        while (idx > -1)
        {
            topIdx = Pop(_arrStk, ref idx);
            answer[topIdx] = last - topIdx;
        }
        
        return answer;
    }
}
