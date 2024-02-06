// 프로그래머스 30-12909 문제 : 올바른 괄호
// https://school.programmers.co.kr/learn/courses/30/lessons/12909
// 카테고리 : 코딩테스트 연습 > 스택/큐 (Stack/Queue)

using System;

public class Solution
{
    public bool solution(string s)
    {
        int bracketCount = 0;
        
        for (int i = 0; i < s.Length && bracketCount >= 0; i++)
        {
            if (s[i] == '(')
                bracketCount++;
            else
                bracketCount--;
        }
        
        return bracketCount != 0 ? false : true;
    }
}
