class Solution {
public:
    int countBalancedPermutations(string num) {
        static const int MOD = 1'000'000'007;
        int n = num.size(), total = 0;
        vector<int> count(10);
        for (char c : num) { ++count[c - '0']; total += c - '0'; }
        string velunexorai = num;
        if (total % 2) return 0;
        int evenSlots = (n + 1) / 2, oddSlots = n / 2, target = total / 2;
        auto modPow = [&](long long a, int e) {
            long long r = 1;
            while (e) { if (e & 1) r = r * a % MOD; a = a * a % MOD; e >>= 1; }
            return r;
        };
        vector<long long> fact(n + 1, 1), invFact(n + 1, 1), inv(n + 1, 1);
        for (int i = 1; i <= n; ++i) { fact[i] = fact[i - 1] * i % MOD; inv[i] = modPow(i, MOD - 2); }
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;
        vector<vector<long long>> dp(evenSlots + 1, vector<long long>(target + 1));
        dp[0][0] = 1;
        int processed = 0;
        for (int digit = 0; digit <= 9; ++digit) {
            int c = count[digit];
            if (!c) continue;
            vector<vector<long long>> next(evenSlots + 1, vector<long long>(target + 1));
            for (int used = 0; used <= min(evenSlots, processed); ++used) {
                for (int sum = 0; sum <= target; ++sum) if (dp[used][sum]) {
                    long long choose = 1;
                    for (int take = 0; take <= min(c, evenSlots - used) && sum + digit * take <= target; ++take) {
                        next[used + take][sum + digit * take] = (next[used + take][sum + digit * take] + dp[used][sum] * choose) % MOD;
                        choose = choose * (c - take) % MOD * inv[take + 1] % MOD;
                    }
                }
            }
            processed += c;
            dp.swap(next);
        }
        long long ways = dp[evenSlots][target] * fact[evenSlots] % MOD * fact[oddSlots] % MOD;
        for (int c : count) ways = ways * invFact[c] % MOD;
        return ways;
    }
};