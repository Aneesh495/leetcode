class Solution {
public:
    int countLocalMaximums(vector<vector<int>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();
        array<vector<pair<int,int>>, 201> positions;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) positions[matrix[r][c]].emplace_back(r,c);
        }
        int answer = 0;
        vector<vector<int>> prefix(rows + 1, vector<int>(cols + 1));
        for (int x = 1; x <= 200; ++x) {
            if (positions[x].empty()) continue;
            for (int r = 0; r < rows; ++r) {
                int withinRow = 0;
                for (int c = 0; c < cols; ++c) {
                    withinRow += matrix[r][c] > x;
                    prefix[r + 1][c + 1] = prefix[r][c + 1] + withinRow;
                }
            }
            for (auto [r,c] : positions[x]) {
                int top = max(0, r - x), bottom = min(rows - 1, r + x);
                int left = max(0, c - x), right = min(cols - 1, c + x);
                int larger = prefix[bottom+1][right+1] - prefix[top][right+1]
                           - prefix[bottom+1][left] + prefix[top][left];
                // Only the true distance-x corners are excluded, even if the box is clipped.
                for (int cornerRow : {r - x, r + x}) {
                    for (int cornerCol : {c - x, c + x}) {
                        if (cornerRow >= 0 && cornerRow < rows && cornerCol >= 0 && cornerCol < cols) {
                            larger -= matrix[cornerRow][cornerCol] > x;
                        }
                    }
                }
                answer += larger == 0;
            }
        }
        return answer;
    }
};