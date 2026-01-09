
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string, int> count;
        for (auto& row : matrix) {
            string key = "";
            for (int j = 0; j < row.size(); ++j)
                key += to_string(row[j] ^ row[0]);
            count[key]++;
        }
        int res = 0;
        for (auto& [k, v] : count) res = max(res, v);
        return res;
    }
};
