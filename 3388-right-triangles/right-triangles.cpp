class Solution {
public:
    long long numberOfRightTriangles(vector<vector<int>>& grid) {
        int rows = grid.size(), columns = grid[0].size();
        vector<int> rowCount(rows), columnCount(columns);
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < columns; ++c) {
                rowCount[r] += grid[r][c];
                columnCount[c] += grid[r][c];
            }
        }
        long long triangles = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < columns; ++c) {
                // Fix the right-angle vertex and choose one other point on each leg.
                if (grid[r][c]) triangles += 1LL * (rowCount[r] - 1) * (columnCount[c] - 1);
            }
        }
        return triangles;
    }
};