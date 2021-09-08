class Solution {
public:
    int minPushBox(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size(), N = m*n, p = 0, b = 0, target = 0;
        for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 'S') p = i*n+j;
            if (grid[i][j] == 'B') b = i*n+j;
            if (grid[i][j] == 'T') target = i*n+j;
        }
        const int INF = 1000000;
        vector<int> dist(N*N, INF);
        deque<pair<int,int>> q;
        dist[p*N+b] = 0; q.push_front({p,b});
        int dr[4] = {1,-1,0,0}, dc[4] = {0,0,1,-1};
        auto valid = [&](int r, int c) { return r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != '#'; };
        while (!q.empty()) {
            auto [player, box] = q.front(); q.pop_front();
            int d = dist[player*N+box];
            if (box == target) return d;
            for (int z = 0; z < 4; ++z) {
                int r = player/n + dr[z], c = player%n + dc[z];
                if (!valid(r,c)) continue;
                int np = r*n+c, nb = box, cost = 0;
                if (np == box) {
                    int br = r+dr[z], bc = c+dc[z];
                    if (!valid(br,bc)) continue;
                    nb = br*n+bc; cost = 1;
                }
                int key = np*N+nb;
                if (d+cost < dist[key]) {
                    dist[key] = d+cost;
                    if (cost) q.push_back({np,nb}); else q.push_front({np,nb});
                }
            }
        }
        return -1;
    }
};