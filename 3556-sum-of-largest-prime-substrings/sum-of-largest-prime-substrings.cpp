class Solution {
public:
    long long sumOfLargestPrimes(string s) {
        auto isPrime = [](long long x) {
            if (x < 2) return false;
            for (long long d = 2; d * d <= x; ++d) if (x % d == 0) return false;
            return true;
        };
        set<long long> st;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            long long v = 0;
            for (int j = i; j < n; ++j) {
                v = v * 10 + (s[j] - '0');
                if (isPrime(v)) st.insert(v);
            }
        }
        long long ans = 0;
        int cnt = 0;
        for (auto it = st.rbegin(); it != st.rend() && cnt < 3; ++it, ++cnt) ans += *it;
        return ans;
    }
};