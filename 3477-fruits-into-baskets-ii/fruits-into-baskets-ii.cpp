class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = fruits.size(), ans = 0;
        vector<bool> used(n, false);
        for (int f : fruits) {
            bool ok = false;
            for (int j = 0; j < n; ++j) {
                if (!used[j] && baskets[j] >= f) { used[j] = true; ok = true; break; }
            }
            if (!ok) ++ans;
        }
        return ans;
    }
};