
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] || grid[n-1][n-1]) return -1;
        queue<pair<int,int>> q;
        q.push({0,0});
        grid[0][0] = 1;
        vector<int> dirs = {-1, 0, 1};
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            int d = grid[x][y];
            if (x == n-1 && y == n-1) return d;
            for (int dx : dirs)
                for (int dy : dirs) {
                    if (!dx && !dy) continue;
                    int nx = x + dx, ny = y + dy;
                    if (nx >= 0 && ny >= 0 && nx < n && ny < n && grid[nx][ny] == 0) {
                        grid[nx][ny] = d + 1;
                        q.push({nx, ny});
                    }
                }
        }
        return -1;
    }
};
