class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dist(n, vector<int>(n, -1));
        queue<pair<int, int>> q;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (grid[i][j] == 1) { dist[i][j] = 0; q.push({i, j}); }
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }
        priority_queue<tuple<int, int, int>> pq;
        vector<vector<int>> best(n, vector<int>(n, -1));
        best[0][0] = dist[0][0];
        pq.push({dist[0][0], 0, 0});
        while (!pq.empty()) {
            auto [s, r, c] = pq.top(); pq.pop();
            if (r == n - 1 && c == n - 1) return s;
            if (s < best[r][c]) continue;
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    int ns = min(s, dist[nr][nc]);
                    if (ns > best[nr][nc]) { best[nr][nc] = ns; pq.push({ns, nr, nc}); }
                }
            }
        }
        return 0;
    }
};
