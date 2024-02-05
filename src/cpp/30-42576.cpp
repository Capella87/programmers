// 프로그래머스 30-42576 문제 : 완주하지 못한 선수
// https://school.programmers.co.kr/learn/courses/30/lessons/42576
// 카테고리 : 코딩테스트 연습 > 해시(Hash)


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string find_halted(vector<string>& parti, vector<string>& comple)
{
    int i = 0;
    size_t comple_count = comple.size();
    
    while (i < comple_count)
    {
        if (parti[i] != comple[i])
        {
            return parti[i];
        }
        i++;
    }
    
    return parti[i];
}

string solution(vector<string> participant, vector<string> completion)
{
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    return find_halted(participant, completion);
}