class Solution {
public:
    vector<int> assignElements(vector<int>& groups, vector<int>& elements) {
        int mx = *max_element(groups.begin(), groups.end());
        vector<int> best(mx + 1, -1);
        vector<bool> seen(mx + 1, false);
        for (int j = 0; j < (int)elements.size(); ++j) {
            int e = elements[j];
            if (e > mx || seen[e]) continue;
            seen[e] = true;
            for (int m = e; m <= mx; m += e) {
                if (best[m] == -1) best[m] = j;
            }
        }
        vector<int> ans(groups.size());
        for (size_t i = 0; i < groups.size(); ++i) ans[i] = best[groups[i]];
        return ans;
    }
};