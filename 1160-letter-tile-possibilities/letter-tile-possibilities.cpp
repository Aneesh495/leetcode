
class Solution {
public:
    int numTilePossibilities(string tiles) {
        vector<int> count(26, 0);
        for (char c : tiles) count[c - 'A']++;
        return dfs(count);
    }
private:
    int dfs(vector<int>& count) {
        int res = 0;
        for (int i = 0; i < 26; ++i) {
            if (count[i] == 0) continue;
            res++;
            count[i]--;
            res += dfs(count);
            count[i]++;
        }
        return res;
    }
};
