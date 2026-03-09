
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) suffix[i] = suffix[i + 1] + piles[i];
        vector<vector<int>> memo(n, vector<int>(n + 1, -1));
        function<int(int,int)> dfs = [&](int i, int M) -> int {
            if (i >= n) return 0;
            if (2 * M >= n - i) return suffix[i];
            int& res = memo[i][M];
            if (res != -1) return res;
            res = 0;
            for (int x = 1; x <= 2 * M; ++x)
                res = max(res, suffix[i] - dfs(i + x, max(M, x)));
            return res;
        };
        return dfs(0, 1);
    }
};
