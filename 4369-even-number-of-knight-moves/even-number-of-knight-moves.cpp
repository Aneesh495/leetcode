class Solution {
public:
    bool canReach(vector<int>& start, vector<int>& target) {
        // A knight changes square color on every move. Check reachability as well.
        if ((start[0] + start[1] + target[0] + target[1]) % 2 != 0) return false;
        const int dr[8] = {1, 1, -1, -1, 2, 2, -2, -2};
        const int dc[8] = {2, -2, 2, -2, 1, -1, 1, -1};
        bool seen[8][8] = {};
        queue<pair<int,int>> next;
        next.emplace(start[0], start[1]);
        seen[start[0]][start[1]] = true;
        while (!next.empty()) {
            auto [row, col] = next.front();
            next.pop();
            if (row == target[0] && col == target[1]) return true;
            for (int d = 0; d < 8; ++d) {
                int nr = row + dr[d], nc = col + dc[d];
                if (nr < 0 || nr >= 8 || nc < 0 || nc >= 8 || seen[nr][nc]) continue;
                seen[nr][nc] = true;
                next.emplace(nr, nc);
            }
        }
        return false;
    }
};