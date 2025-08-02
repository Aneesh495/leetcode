class Solution {
    vector<int> zFunction(const string& t) {
        int n = (int)t.size();
        vector<int> z(n);
        int left = 0, right = 0;
        for (int i = 1; i < n; ++i) {
            if (i <= right) z[i] = min(right - i + 1, z[i - left]);
            while (i + z[i] < n && t[z[i]] == t[i + z[i]]) ++z[i];
            if (i + z[i] - 1 > right) {
                left = i;
                right = i + z[i] - 1;
            }
        }
        return z;
    }
public:
    int minStartingIndex(string s, string pattern) {
        int n = (int)s.size(), m = (int)pattern.size();
        string forward = pattern + "#" + s;
        vector<int> pref = zFunction(forward);
        string revPattern(pattern.rbegin(), pattern.rend());
        string revS(s.rbegin(), s.rend());
        string backward = revPattern + "#" + revS;
        vector<int> suff = zFunction(backward);
        for (int i = 0; i + m <= n; ++i) {
            int leftMatch = min(m, pref[m + 1 + i]);
            if (leftMatch == m) return i;
            int reverseStart = n - (i + m);
            int rightMatch = min(m, suff[m + 1 + reverseStart]);
            if (leftMatch + rightMatch >= m - 1) return i;
        }
        return -1;
    }
};