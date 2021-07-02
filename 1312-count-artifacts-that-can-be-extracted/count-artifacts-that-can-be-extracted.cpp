class Solution {
public:
    int digArtifacts(int n, vector<vector<int>>& artifacts, vector<vector<int>>& dig) {
        vector<bool> dug(n * n);
        for (const auto& cell : dig) dug[cell[0] * n + cell[1]] = true;
        int extracted = 0;
        for (const auto& a : artifacts) {
            bool complete = true;
            // Each artifact covers at most four cells, so check them directly.
            for (int r = a[0]; r <= a[2]; ++r) {
                for (int c = a[1]; c <= a[3]; ++c) {
                    complete = complete && dug[r * n + c];
                }
            }
            extracted += complete;
        }
        return extracted;
    }
};