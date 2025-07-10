class Solution {
public:
    vector<vector<int>> specialGrid(int n) {
        int N = 1 << n;
        vector<vector<int>> g(N, vector<int>(N));
        int cur = 0;
        auto dfs = [&](auto& self, int r, int c, int sz) -> void {
            if (sz == 1) { g[r][c] = cur++; return; }
            int h = sz / 2;
            self(self, r, c + h, h);
            self(self, r + h, c + h, h);
            self(self, r + h, c, h);
            self(self, r, c, h);
        };
        dfs(dfs, 0, 0, N);
        return g;
    }
};