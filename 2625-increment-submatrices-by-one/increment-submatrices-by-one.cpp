class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> mat(n + 1, vector<int>(n + 1, 0));
        for (const auto& q : queries) {
            mat[q[0]][q[1]]++;
            mat[q[0]][q[3] + 1]--;
            mat[q[2] + 1][q[1]]--;
            mat[q[2] + 1][q[3] + 1]++;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i > 0) mat[i][j] += mat[i - 1][j];
                if (j > 0) mat[i][j] += mat[i][j - 1];
                if (i > 0 && j > 0) mat[i][j] -= mat[i - 1][j - 1];
            }
        }
        mat.resize(n);
        for (auto& r : mat) r.resize(n);
        return mat;
    }
};
