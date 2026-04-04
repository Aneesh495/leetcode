
class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> left(m, vector<int>(n, 0)), up(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (grid[i][j]) {
                    left[i][j] = (j ? left[i][j - 1] : 0) + 1;
                    up[i][j] = (i ? up[i - 1][j] : 0) + 1;
                }
        int best = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int small = min(left[i][j], up[i][j]);
                while (small > best) {
                    int topRow = i - small + 1, leftCol = j - small + 1;
                    if (up[i][leftCol] >= small && left[topRow][j] >= small) {
                        best = small;
                        break;
                    }
                    small--;
                }
            }
        }
        return best * best;
    }
};
