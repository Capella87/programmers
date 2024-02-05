// 프로그래머스 30-42577 문제 : 전화번호 목록
// https://school.programmers.co.kr/learn/courses/30/lessons/42577
// 카테고리 : 코딩테스트 연습 > 해시(Hash)

// Use trie structure

#include <string>
#include <vector>

using namespace std;

typedef struct trie
{
    struct trie* nums[10];
    char num;
    bool is_end_of_word;
    int subnode_count;
} trie;

trie* trie_init(void)
{
    trie* rt = new trie;
    for (int i = 0; i < 10; i++)
    {
        rt->nums[i] = NULL;
    }
    rt->num = -1; // it means the node is root;
    rt->is_end_of_word = false;
    rt->subnode_count = 0;
    
    return rt;
}

trie* trie_add(trie* tr, char num)
{
    trie* trie_new = trie_init();
    trie_new->num = num;
    tr->nums[num - '0'] = trie_new;
    tr->subnode_count++;
    
    return trie_new;
}

bool trie_try_find(trie* tr, string target)
{
    trie* cursor = tr;
    
    size_t target_len = target.size();
    char char_loc = 0;
    for (size_t i = 0; i < target_len; i++)
    {
        char_loc = target[i] - '0';
        if (cursor->nums[char_loc] == NULL)
        {
            cursor = trie_add(cursor, target[i]);
        }
        else
        {
            cursor = cursor->nums[char_loc];
            
            if (cursor->is_end_of_word)
                return true;
        }
        
    }
    
    cursor->is_end_of_word = true;
    // 생성 안 하고 이전 번호보다 짧게 끝나는 경우
    if (cursor->subnode_count > 0)
        return true;
    
    return false;
}

bool get_answer(vector<string>& book)
{
    trie* tr = trie_init();
    
    size_t len = book.size();
    
    for (size_t i = 0; i < len; i++)
    {
        size_t pnumber_len = book[i].size();
        
        if (trie_try_find(tr, book[i]))
            return false;
    }
    
    return true;
}


bool solution(vector<string> phone_book) {
    return get_answer(phone_book);
}