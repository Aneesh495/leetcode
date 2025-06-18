class Solution {
public:
    int longestPalindrome(string s, string t) {
        auto isPal = [](const string& str) {
            int l = 0, r = (int)str.size() - 1;
            while (l < r) if (str[l++] != str[r--]) return false;
            return true;
        };
        int ans = 1, ns = s.size(), nt = t.size();
        for (int i = 0; i <= ns; ++i) for (int j = i; j <= ns; ++j) {
            string a = s.substr(i, j - i);
            for (int p = 0; p <= nt; ++p) for (int q = p; q <= nt; ++q) {
                string c = a + t.substr(p, q - p);
                if ((int)c.size() > ans && isPal(c)) ans = c.size();
            }
        }
        return ans;
    }
};