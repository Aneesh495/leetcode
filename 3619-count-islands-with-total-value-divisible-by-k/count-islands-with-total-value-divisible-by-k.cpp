class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size(), ans = 0;
        int dr[4] = {0, 0, 1, -1}, dc[4] = {1, -1, 0, 0};
        for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) if (grid[i][j] > 0) {
            long long sum = 0;
            queue<pair<int, int>> q;
            sum += grid[i][j]; grid[i][j] = 0; q.push({i, j});
            while (!q.empty()) {
                auto [r, c] = q.front(); q.pop();
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d], nc = c + dc[d];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                        sum += grid[nr][nc]; grid[nr][nc] = 0; q.push({nr, nc});
                    }
                }
            }
            if (sum % k == 0) ++ans;
        }
        return ans;
    }
};