class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        int n = s.size();
        vector<int> first(26, n), last(26, -1);
        for (int i = 0; i < n; ++i) {
            first[s[i] - 'a'] = min(first[s[i] - 'a'], i);
            last[s[i] - 'a'] = max(last[s[i] - 'a'], i);
        }
        vector<pair<int, int>> ivs;
        for (int c = 0; c < 26; ++c) {
            if (last[c] == -1) continue;
            int l = first[c], r = last[c];
            bool ok = true;
            for (int i = l; i <= r; ++i) {
                int ch = s[i] - 'a';
                if (first[ch] < l) { ok = false; break; }
                r = max(r, last[ch]);
            }
            if (ok && r - l + 1 < n) ivs.push_back({r, l});
        }
        sort(ivs.begin(), ivs.end());
        int cnt = 0, cur = -1;
        for (auto& [r, l] : ivs) {
            if (l > cur) { ++cnt; cur = r; }
        }
        return cnt >= k;
    }
};