class Solution {
public:
    int countKSubsequencesWithMaxBeauty(string s, int k) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        vector<int> f;
        for (int c : cnt) if (c > 0) f.push_back(c);
        if ((int)f.size() < k) return 0;
        sort(f.rbegin(), f.rend());
        const long long MOD = 1e9 + 7;
        int kth = f[k - 1], tie = 0, need = 0;
        long long ans = 1;
        for (int i = 0; i < (int)f.size(); ++i) {
            if (f[i] > kth) ans = ans * f[i] % MOD;
            else if (f[i] == kth) { tie++; if (i < k) need++; }
        }
        long long C[27][27] = {};
        for (int i = 0; i <= 26; ++i) {
            C[i][0] = 1;
            for (int j = 1; j <= i; ++j) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
        ans = ans * C[tie][need] % MOD;
        for (int i = 0; i < need; ++i) ans = ans * kth % MOD;
        return ans;
    }
};
