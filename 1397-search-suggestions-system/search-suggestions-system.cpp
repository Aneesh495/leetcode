class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> ans;
        string prefix;
        for (char c : searchWord) {
            prefix += c;
            auto it = lower_bound(products.begin(), products.end(), prefix);
            vector<string> row;
            for (int i = 0; i < 3 && it != products.end(); ++i, ++it) {
                if (it->compare(0, prefix.size(), prefix) != 0) break;
                row.push_back(*it);
            }
            ans.push_back(row);
        }
        return ans;
    }
};