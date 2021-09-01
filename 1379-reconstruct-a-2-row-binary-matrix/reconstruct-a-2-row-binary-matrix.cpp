class Solution {
public:
    vector<vector<int>> reconstructMatrix(int upper, int lower, vector<int>& colsum) {
        int n = colsum.size();
        vector<vector<int>> a(2, vector<int>(n));
        for (int i = 0; i < n; ++i) if (colsum[i] == 2) {
            a[0][i] = a[1][i] = 1; --upper; --lower;
        }
        if (upper < 0 || lower < 0) return {};
        for (int i = 0; i < n; ++i) if (colsum[i] == 1) {
            if (upper > 0) { a[0][i] = 1; --upper; }
            else { a[1][i] = 1; --lower; }
        }
        return upper == 0 && lower == 0 ? a : vector<vector<int>>{};
    }
};