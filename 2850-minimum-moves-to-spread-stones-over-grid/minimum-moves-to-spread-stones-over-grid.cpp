class Solution {
public:
    int minimumMoves(vector<vector<int>>& grid) {
        vector<pair<int, int>> zeros, extras;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (grid[i][j] == 0) zeros.push_back({i, j});
                else for (int k = 1; k < grid[i][j]; ++k) extras.push_back({i, j});
            }
        }
        sort(extras.begin(), extras.end());
        int ans = INT_MAX;
        do {
            int cur = 0;
            for (int i = 0; i < (int)zeros.size(); ++i) {
                cur += abs(zeros[i].first - extras[i].first) + abs(zeros[i].second - extras[i].second);
            }
            ans = min(ans, cur);
        } while (next_permutation(extras.begin(), extras.end()));
        return ans;
    }
};
