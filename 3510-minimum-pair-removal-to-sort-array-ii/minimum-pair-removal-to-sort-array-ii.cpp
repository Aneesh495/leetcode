class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        vector<long long> val(nums.begin(), nums.end());
        vector<int> prv(n), nxt(n);
        iota(prv.begin(), prv.end(), -1);
        for (int i = 0; i < n; ++i) nxt[i] = (i + 1 < n ? i + 1 : -1);
        int bad = 0;
        set<pair<long long, int>> st;
        for (int i = 0; i + 1 < n; ++i) {
            if (val[i] > val[i + 1]) ++bad;
            st.insert({val[i] + val[i + 1], i});
        }
        int ans = 0;
        while (bad > 0) {
            auto [s, i] = *st.begin(); st.erase(st.begin());
            int j = nxt[i], L = prv[i], R = nxt[j];
            if (L != -1) { st.erase({val[L] + val[i], L}); if (val[L] > val[i]) --bad; }
            if (val[i] > val[j]) --bad;
            if (R != -1) { st.erase({val[j] + val[R], j}); if (val[j] > val[R]) --bad; }
            val[i] = s;
            nxt[i] = R;
            if (R != -1) prv[R] = i;
            if (L != -1) { st.insert({val[L] + val[i], L}); if (val[L] > val[i]) ++bad; }
            if (R != -1) { st.insert({val[i] + val[R], i}); if (val[i] > val[R]) ++bad; }
            ++ans;
        }
        return ans;
    }
};