// 프로그래머스 30-42883 문제 : 큰 수 만들기
// https://programmers.co.kr/learn/courses/30/lessons/42883
// 카테고리 : 코딩테스트 연습 > 탐욕법(Greedy)

using System;

public class Solution
{
    public string solution(string number, int k)
    {
        char[] result = new char[number.Length - k];
        result[0] = number[0];
        int resultIdx = 0;

        for (int i = 1; i < number.Length; i++)
        {
            int prev = result[resultIdx] - '0';
            int digit = number[i] - '0';

            if (prev < digit)
            {
                while (resultIdx >= 0 && (result[resultIdx] - '0') < (number[i] - '0') && k > 0)
                {
                    k--;
                    prev = result[resultIdx] - '0';
                    resultIdx--;
                }
            }
            if (++resultIdx == result.Length)
            {
                k--;
                prev = result[--resultIdx] - '0';
                if (prev > digit) continue;
            }
            result[resultIdx] = number[i];
        }
        return new string(result);
    }
}
