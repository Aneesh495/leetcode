class Solution {
    int k;
    int solve(int n) {
        string s = to_string(n);
        int m = s.size();
        int memo[11][22][21][2][2];
        memset(memo, -1, sizeof(memo));
        auto dfs = [&](auto& self, int i, int diff, int rem, bool tight, bool started) -> int {
            if (i == m) return (started && diff == 10 && rem == 0) ? 1 : 0;
            int& res = memo[i][diff][rem][tight][started];
            if (res != -1) return res;
            res = 0;
            int lim = tight ? (s[i] - '0') : 9;
            for (int d = 0; d <= lim; ++d) {
                bool nt = tight && (d == lim);
                if (!started && d == 0) {
                    res += self(self, i + 1, diff, rem, nt, false);
                } else {
                    res += self(self, i + 1, diff + (d % 2 == 0 ? 1 : -1), (rem * 10 + d) % k, nt, true);
                }
            }
            return res;
        };
        return dfs(dfs, 0, 10, 0, true, false);
    }
public:
    int numberOfBeautifulIntegers(int low, int high, int k) {
        this->k = k;
        return solve(high) - solve(low - 1);
    }
};
