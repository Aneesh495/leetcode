class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int n = nums.size(), sumMax = 0;
        for (int x : nums) sumMax += x;
        if (abs(k) > sumMax) return -1;
        unordered_map<int, unordered_set<int>> dp;
        for (int x : nums) {
            auto ndp = dp;
            auto addState = [&](int key, int prod) {
                if (prod > limit) prod = limit + 1;
                ndp[key].insert(prod);
            };
            addState(((x) << 1) | 1, x);
            for (auto& [key, st] : dp) {
                int s = key >> 1, par = key & 1;
                int ns = par ? (s - x) : (s + x);
                int nkey = (ns << 1) | (par ^ 1);
                for (int p : st) addState(nkey, p * x);
            }
            dp.swap(ndp);
        }
        int ans = -1;
        for (int par : {0, 1}) {
            auto it = dp.find((k << 1) | par);
            if (it != dp.end()) {
                for (int p : it->second) if (p <= limit) ans = max(ans, p);
            }
        }
        return ans;
    }
};