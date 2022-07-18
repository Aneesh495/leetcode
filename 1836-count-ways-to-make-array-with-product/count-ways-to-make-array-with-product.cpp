class Solution {
public:
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        constexpr long long mod = 1000000007;
        // No prime factor can occur more than 13 times when k <= 10,000.
        constexpr int maxExponent = 13;
        long long inverse[maxExponent + 1] = {0, 1};
        for (int i = 2; i <= maxExponent; ++i) {
            inverse[i] = mod - (mod / i) * inverse[mod % i] % mod;
        }

        vector<int> answer;
        answer.reserve(queries.size());
        for (const auto& query : queries) {
            const int n = query[0];
            int k = query[1];
            long long ways = 1;
            for (int prime = 2; prime * prime <= k; ++prime) {
                int exponent = 0;
                while (k % prime == 0) {
                    k /= prime;
                    ++exponent;
                }
                // Distribute this prime's copies independently: C(n + exponent - 1, exponent).
                for (int i = 1; i <= exponent; ++i) {
                    ways = ways * (n + i - 1) % mod * inverse[i] % mod;
                }
            }
            if (k > 1) {
                ways = ways * n % mod;
            }
            answer.push_back(static_cast<int>(ways));
        }
        return answer;
    }
};