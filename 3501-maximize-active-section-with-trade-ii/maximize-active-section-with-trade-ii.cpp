class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        int total1 = 0;
        for (char c : s) if (c == '1') total1++;
        vector<int> L, R, blk(n, -1);
        for (int i = 0; i < n; ) {
            if (s[i] == '0') {
                int j = i;
                while (j < n && s[j] == '0') { blk[j] = L.size(); j++; }
                L.push_back(i); R.push_back(j - 1);
                i = j;
            } else i++;
        }
        int m = L.size();
        vector<int> next0(n, m), prev0(n, -1);
        for (int i = n - 1, cur = m; i >= 0; --i) {
            if (blk[i] != -1) cur = blk[i];
            next0[i] = cur;
        }
        for (int i = 0, cur = -1; i < n; ++i) {
            if (blk[i] != -1) cur = blk[i];
            prev0[i] = cur;
        }
        int k = max(0, m - 1);
        int LOG = 1;
        while ((1 << LOG) <= max(1, k)) LOG++;
        vector<vector<int>> st(LOG, vector<int>(max(1, k), 0));
        for (int i = 0; i < k; ++i) st[0][i] = (R[i] - L[i] + 1) + (R[i + 1] - L[i + 1] + 1);
        for (int j = 1; j < LOG; ++j)
            for (int i = 0; i + (1 << j) <= k; ++i)
                st[j][i] = max(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
        auto rmq = [&](int l, int r) {
            if (l > r) return 0;
            int j = 31 - __builtin_clz(r - l + 1);
            return max(st[j][l], st[j][r - (1 << j) + 1]);
        };
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            int z0 = next0[l], z1 = prev0[r];
            int gain = 0;
            if (z0 < z1) {
                int len0 = min(R[z0], r) - max(L[z0], l) + 1;
                int len1 = min(R[z1], r) - max(L[z1], l) + 1;
                if (z0 + 1 == z1) gain = len0 + len1;
                else {
                    gain = max(len0 + (R[z0 + 1] - L[z0 + 1] + 1), (R[z1 - 1] - L[z1 - 1] + 1) + len1);
                    if (z0 + 1 <= z1 - 2) gain = max(gain, rmq(z0 + 1, z1 - 2));
                }
            }
            ans.push_back(total1 + gain);
        }
        return ans;
    }
};