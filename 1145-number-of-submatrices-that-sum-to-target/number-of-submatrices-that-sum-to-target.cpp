
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size(), res = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 1; j < n; ++j)
                matrix[i][j] += matrix[i][j - 1];
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                unordered_map<int, int> count;
                count[0] = 1;
                int cur = 0;
                for (int k = 0; k < m; ++k) {
                    cur += matrix[k][j] - (i > 0 ? matrix[k][i - 1] : 0);
                    res += count[cur - target];
                    count[cur]++;
                }
            }
        }
        return res;
    }
};
