// 프로그래머스 30-42860 문제 : 조이스틱
// https://programmers.co.kr/learn/courses/30/lessons/42860
// 카테고리 : 코딩테스트 연습 > 탐욕법(Greedy)

using System;

public class Solution
{
    public int solution(string name)
    {
        int answer = 0;
        int move = name.Length - 1;

        for (int i = 0; i < name.Length; i++)
        {
            int idx = i + 1;
            while (idx < name.Length && name[idx] == 'A')
            {
                idx++;
            }

            move = Math.Min(move, (i * 2) + name.Length - idx);
            move = Math.Min(move, (name.Length - idx) * 2 + i);

            // Counts the distance from A to the targeted character.
            answer += GetCharacterDistance(name[i]);
        }
        answer += move;
        return answer;
    }

    public int GetCharacterDistance(char target)
    {
        // Move Up for 25 times to reach from 'A' to 'Z'
        int upMoves = target - 'A';
        // Move Down only 1 time to reach to 'Z'
        int downMoves = 26 - upMoves;

        return Math.Min(upMoves, downMoves);
    }
}
