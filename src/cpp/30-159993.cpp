// 프로그래머스 30-159993 문제 : 미로 탈출
// https://school.programmers.co.kr/learn/courses/30/lessons/159993

// 분류 : BFS

#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <iostream>

using namespace std;

const int xMove[4] = { 0, 1, 0, -1 };
const int yMove[4] = { 1, 0, -1, 0 };

pair<int, int> get_coordinates(vector<string>& map, char target, size_t height, size_t width)
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (map[i][j] == target)
            {
                return { i, j };
            }
        }
    }
    return { -1, -1 };
}

vector<vector<int>> get_visitmap(size_t height, size_t width)
{
    vector<vector<int>> mp = vector<vector<int>>(height, vector<int>(width, false));
    return mp;
}

int bfs(vector<string>& map, pair<int, int>& start, pair<int, int>& dest, size_t height, size_t width)
{
    queue<tuple<int, int, int>> q;
    vector<vector<int>> visit = get_visitmap(height, width);

    q.push({ start.first, start.second, 0 });
    while (q.size() > 0)
    {
        tuple <int, int, int> cur = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int new_x = get<0>(cur) + xMove[i];
            int new_y = get<1>(cur) + yMove[i];
            if (new_x < 0 || new_y < 0 || new_x >= height || new_y >= width) continue;
            if (new_x == dest.first && new_y == dest.second)
            {
                visit[new_x][new_y] = get<2>(cur) + 1;
                return visit[new_x][new_y];
            }
            if (map[new_x][new_y] != 'X' && visit[new_x][new_y] == 0)
            {
                visit[new_x][new_y] = get<2>(cur) + 1;
                q.push({ new_x, new_y, visit[new_x][new_y] });
            }
        }
    }
    if (visit[dest.first][dest.second] == 0) return -1;
    return visit[dest.first][dest.second];
}

int solution(vector<string> maps)
{
    int answer = 0;

    size_t height = maps.size();
    size_t width = maps[0].size();

    pair<int, int> dest = get_coordinates(maps, 'E', height, width);
    pair<int, int> lever_loc = get_coordinates(maps, 'L', height, width);
    pair<int, int> start_loc = get_coordinates(maps, 'S', height, width);

    int l = bfs(maps, start_loc, lever_loc, height, width);
    int d = bfs(maps, lever_loc, dest, height, width);

    if (l == -1 || d == -1) return -1;
    return l + d;
}
