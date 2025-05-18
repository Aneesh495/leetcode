class Solution {
public:
    bool hasSameDigits(string s) {
        int n = s.size() - 2;
        int C5[5][5] = {0};
        for (int i = 0; i < 5; ++i) { C5[i][0] = 1; for (int j = 1; j <= i; ++j) C5[i][j] = (C5[i - 1][j - 1] + C5[i - 1][j]) % 5; }
        auto lucas5 = [&](int a, int b) {
            int res = 1;
            while (a > 0 || b > 0) {
                int aa = a % 5, bb = b % 5;
                if (bb > aa) return 0;
                res = (res * C5[aa][bb]) % 5;
                a /= 5; b /= 5;
            }
            return res;
        };
        int diff = 0;
        for (int i = 0; i <= n; ++i) {
            int m2 = ((n & i) == i) ? 1 : 0;
            int m5 = lucas5(n, i);
            int c = (m2 * 5 + m5 * 6) % 10;
            diff = (diff + c * (s[i] - s[i + 1])) % 10;
        }
        return (diff % 10 + 10) % 10 == 0;
    }
};