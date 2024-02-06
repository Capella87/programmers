// 프로그래머스 30-12906 문제 : 같은 숫자는 싫어
// https://school.programmers.co.kr/learn/courses/30/lessons/12906
// 카테고리 : 코딩테스트 연습 > 스택/큐 (Stack/Queue)

#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    answer.push_back(arr[0]);
    int cursor = arr[0];
    size_t len = arr.size();
    
    for (int i = 0; i < len; i++)
    {
        if (arr[i] == cursor)
        {
            continue;
        }
        
        cursor = arr[i];
        answer.push_back(cursor);
    }

    return answer;
}
