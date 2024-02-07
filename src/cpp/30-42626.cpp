// 프로그래머스 30-42626 문제 : 더 맵게
// https://school.programmers.co.kr/learn/courses/30/lessons/42626
// 카테고리 : 코딩테스트 연습 > 힙(Heap)

#include <string>
#include <vector>
#include <queue>
#define MIX_FOOD(a, b) ((a) + ((b) * 2))

using namespace std;

int solution(vector<int> scoville, int K)
{
    // Make a min heap
    priority_queue<int, vector<int>, greater<int>> scoville_queue(begin(scoville), end(scoville));
    int top = 0, second = 0;
    int count = 0;
    
    while (scoville_queue.size() > 1 && (top = scoville_queue.top()) < K)
    {
        scoville_queue.pop();
        second = scoville_queue.top();
        scoville_queue.pop();
        scoville_queue.push(MIX_FOOD(top, second));
        count++;
    }
    
    return scoville_queue.top() < K ? -1 : count;
}
