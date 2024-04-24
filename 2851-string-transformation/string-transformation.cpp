class Solution {
public:
    int numberOfWays(string s, string t, long long k) {
        int n = s.size();
        string ss = s + s;
        ss.pop_back();
        vector<int> pi(n, 0);
        for (int i = 1, j = 0; i < n; ++i) {
            while (j > 0 && t[i] != t[j]) j = pi[j - 1];
            if (t[i] == t[j]) j++;
            pi[i] = j;
        }
        int c = 0;
        for (int i = 0, j = 0; i < (int)ss.size(); ++i) {
            while (j > 0 && ss[i] != t[j]) j = pi[j - 1];
            if (ss[i] == t[j]) j++;
            if (j == n) { c++; j = pi[j - 1]; }
        }
        const long long MOD = 1e9 + 7;
        auto mul = [&](const array<array<long long, 2>, 2>& A, const array<array<long long, 2>, 2>& B) {
            array<array<long long, 2>, 2> C = {{{0, 0}, {0, 0}}};
            for (int i = 0; i < 2; ++i)
                for (int j = 0; j < 2; ++j)
                    for (int l = 0; l < 2; ++l)
                        C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD;
            return C;
        };
        array<array<long long, 2>, 2> M = {{{c - 1, c}, {n - c, n - 1 - c}}};
        array<array<long long, 2>, 2> res = {{{1, 0}, {0, 1}}};
        for (long long e = k; e > 0; e >>= 1) {
            if (e & 1) res = mul(res, M);
            M = mul(M, M);
        }
        return s == t ? res[0][0] : res[0][1];
    }
};
